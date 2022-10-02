import os

from flask import Flask
from flask import render_template
from flask import request
from subprocess import run


def create_app(test_config=None):

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def change_smb_pwd():
        return render_template('change_pwd.html')

    @app.route('/change/', methods=['POST'])
    def exec_change_smb_pwd():
        if request.method == 'POST':
            form_data = request.form
            username = form_data['username']
            current_password = form_data['current_password']
            new_password = form_data['new_password']
            second_new_password = form_data['second_new_password']

            issues = list()
            if new_password != second_new_password:
                issues.append('Incorrect password retype. New passwords do not match.')
            if not username:
                issues.append('Username cannot be empty')
            if not new_password:
                issues.append('New password cannot be empty.')

            if len(issues) > 0:
                return render_template('issues.html', issues=issues)

            ret_val = None
            err_message = ''

            # concatenate both current and passwords with EOLs after each and encode in byte stream using UTF-8
            passwords_as_input = current_password + '\n' + new_password + '\n'
            # used command is smbpasswd -s -U <user>
            # passwords are redirected from stdin
            try:
                ret_val = run(['smbpasswd', '-s', '-U', username], input=passwords_as_input.encode())
            except OSError as err:
                err_message = '{0}'.format(err)

            if err_message != '':
                return render_template('issues.html', issues=[err_message])
            if ret_val.returncode != 0:
                return render_template('issues.html', issues=[ret_val.stderr])

            return 'Samba password for {} has been successfully changed'.format(username)

    return app
