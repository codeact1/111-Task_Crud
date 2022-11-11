import requests

BASE_URL = "http://127.0.0.1:5000/tasks/"

def delete_task(pk):
    url = "%s%s" % (BASE_URL, pk)
    response = requests.delete(url)
    if response.status_code == 204:
        print("Delete successful.")
    else:
        print("Something went wrong while trying to delete task.")

if __name__ == "__main__":
    task_id = input("Target task id: ")
    delete_task(task_id)        