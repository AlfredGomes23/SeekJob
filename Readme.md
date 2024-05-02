# SeekJob dependencies
	
	Package                 Version (or later)
    -------------------------------------------
    asgiref                 3.8.1
    asttokens               2.4.1
    colorama                0.4.6
    comm                    0.2.1
    debugpy                 1.8.1
    decorator               5.1.1
    Django                  4.2.6
    django-crispy-forms     2.0
    django-recaptcha        4.0.0
    executing               2.0.1
    ipykernel               6.29.2
    ipython                 8.21.0
    jedi                    0.19.1
    jupyter_client          8.6.0
    jupyter_core            5.7.1
    matplotlib-inline       0.1.6
    nest-asyncio            1.6.0
    packaging               23.2
    parso                   0.8.3
    Pillow                  10.0.1
    platformdirs            4.2.0
    prompt-toolkit          3.0.43
    psutil                  5.9.8
    pure-eval               0.2.2
    Pygments                2.17.2
    python-dateutil         2.8.2
    pywin32                 306
    pyzmq                   25.1.2
    six                     1.16.0
    sqlparse                0.4.4
    stack-data              0.6.3
    tornado                 6.4
    traitlets               5.14.1
    tzdata                  2024.1
    wcwidth                 0.2.13



#   Installation and Setup
Commands to setup the projects in VSCode -
At any directory, open the VSCode terminal or the Windows’s cmd/terminal and run the following commands sequentially-

    1. git clone https://github.com/AlfredGomes23/SeekJob.git
    2. cd .\SeekJob
    3. python -m venv venv
    4. venv\Scripts\activate
    5. cd .\mysite
    6. pip install -r requirements.txt
    7. python .\manage.py runserver
Then visit http://localhost:8000

*The same commands can be followed for PyCharm’s terminal.


# Features
-----User-----
  1.	SignUp
  2.	Login
  3.	Create Candidate/Recruiter Profile
  4.	Edit profile
  5.	Upload Resume(candidate)

-----Job-----
  1.	Post
  2.	View Details
  3.	Delate

# Note
The Design Credit goes to its original creator, here we are using  template for our Academic Project only.
