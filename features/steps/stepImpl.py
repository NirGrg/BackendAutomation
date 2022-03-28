import requests
from behave import *

import utilities.configurations
from payLoad import addBookPayLoad
from utilities.configurations import *
from utilities.resources import *


@given('Book details which needs to be added to Library')
def step_Impl(context):
    context.url_add = getConfig()['API']['endpoint'] + APIResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = addBookPayLoad("adfluej", "123e")


@when('we execute the AddBook PostAPI Method')
def step_Impl(context):
    context.addBook_response = requests.post(context.url_add, json=context.payLoad, headers=context.headers, )


@then('Book is successfully added')
def step_Impl(context):
    print(context.addBook_response.json())
    response_json = context.addBook_response.json()

    context.book_Id = response_json['ID']
    print(context.book_Id)
    assert response_json["Msg"] == "successfully added"


@given('Book details with {isbn} and {aisle}')
def step_Impl(context, isbn, aisle):
    context.url_add = utilities.configurations.getConfig()['API']['endpoint'] + APIResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = addBookPayLoad(isbn, aisle)
