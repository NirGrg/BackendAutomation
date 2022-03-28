import requests

from utilities.configurations import getConfig
from utilities.resources import APIResources


def after_scenario(context, scenario):
    delete_book_response = requests.post('http://216.10.245.166/Library/DeleteBook.php', json={
        "ID": context.book_Id}, headers={"Content-Type": "application/json"}, )

    assert delete_book_response.status_code == 200
    res_json = delete_book_response.json()

    print(res_json["msg"])
    assert res_json["msg"] == "book is successfully deleted"
