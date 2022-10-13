import pytest
import os
import smtplib

'''
pytsst fixture 주 사용 경우
- 테스트를 위한 데이터 셋업과 테이터 클리닝이 반복적, 독립적으로 사용될 경우

fixture 실제 사용 예시
- 테스트를 위한 특정 파일과 디렉토리를 만들고 테스트 종료 시 해당 파일과 디렉트로리를 삭제한다.
- DB를 연결하고 테스트 종료 시 DB 연결을 정상적으로 종료한다.

사용사례 가정
1. 테스트를 위한 임시 디렉토리와 파일을 생성
2. 임시 파일에 데이터를 수집되었다는 것을 의미한다.
3. 데이터를 입력 완료 후 임시 디렉토리와 파일을 생성
4. 테스트 종료
'''

@pytest.fixture
def make_directory_and_txt_file_yield():
    directory_name = "/data/"
    directory_path = os.getcwd()+directory_name
    try:
        if not(os.path.isdir(directory_path)):
            os.makedirs(os.path.join(directory_path))
            print("\nmake directory", directory_path)
    except Exception as e:
        print("make_directory() has errer \n error message: {}".format(e))

    file_name = "temp_data.txt"
    full_file_path = directory_path+file_name
    print("make file", file_name)
    f = open(full_file_path, 'w')
    yield f

    f.close()
    os.remove(full_file_path)
    print('\ndelete temp file ', full_file_path)
    os.rmdir(directory_path)
    print("delete directory ", directory_path)
    print("teardown complete")


def test_file_write_yield(make_directory_and_txt_file_yield):
    file_pointer = make_directory_and_txt_file_yield
    file_pointer.write("data write")
    print("data write to file")


# request.addfianlizer를 활용한 teardown
@pytest.fixture
def make_directory_and_txt_file_addfinalizer(request):
    directory_name = "/data/"
    directory_path = os.getcwd()+directory_name
    try:
        if not(os.path.isdir(directory_path)):
            os.makedirs(os.path.join(directory_path))
            print("\nmake directory ", directory_path)
    except Exception as e:
        print("make directory() has error \n error message: {}".format(e))

    file_name = "temp_data.txt"
    print("make file", file_name)
    full_file_path = directory_path+file_name
    f = open(full_file_path, 'w')

    def teardown():
        f.close()
        os.remove(full_file_path)
        print("\ndelete temp file ", full_file_path)
        os.rmdir(directory_path)
        print("delete directory ", directory_path)
        print("teardown complete")

    request.addfinalizer(teardown)

    return f


def test_file_write_addfinalizer(make_directory_and_txt_file_addfinalizer):
    file_pointer = make_directory_and_txt_file_addfinalizer
    file_pointer.write("data write")
    print("data write to file")