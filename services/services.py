import requests


def login(email, password, userType):
    url = f"http://localhost:8000/login/{userType}"

    payload = {
        "email": email,
        "password": password
    }

    response = requests.request("POST", url, json=payload, timeout=60)
    return response.json()['status']


def enrollCourse(courseName):
    url = f"http://localhost:8000/enrollCourse/{courseName}"

    response = requests.request("POST", url, timeout=60)
    return response.json()


def submit(data, pageName):
    url = f"http://localhost:8000/submit/{pageName}"

    response = requests.request("POST", url, json=data, timeout=60)
    return response.json()


def getStudents():
    url = f"http://localhost:8000/getData/students"
    response = requests.request("GET", url, timeout=60)
    return response.json()


def getAssignments():
    url = f"http://localhost:8000/getData/assignment"
    response = requests.request("GET", url, timeout=60)
    return response.json()


def getQuizzes():
    url = f"http://localhost:8000/getData/quiz"
    response = requests.request("GET", url, timeout=60)
    return response.json()


def getFeedback():
    url = f"http://localhost:8000/getData/feedback"
    response = requests.request("GET", url, timeout=60)
    return response.json()


def uploadFile(name, path, ext, userType, fileType):
    url = f"http://localhost:8000/upload/{userType}?filetype={fileType}"

    payload = {}
    files = [
        ('file', (name, open(path, 'rb'), f'application/{ext}'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files, timeout=60)

    return response.json()


def download_file(file_path, path):
    # Display a file dialog box to allow the user to select the download location

    # Download the file from the URL
    url = f'http://localhost:8000/{path}'
    response = requests.get(url, timeout=60)

    # Write the downloaded file to disk
    with open(file_path, 'wb') as f:
        f.write(response.content)
