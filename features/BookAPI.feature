# Created by Nir.Gurung at 3/25/2022
Feature: Verify If Books are added and deleted using Library API

  Scenario: Verify AddBook API Functionality
    Given Book details which needs to be added to Library
    When we execute the AddBook PostAPI Method
    Then Book is successfully added

  Scenario Outline:
    Given Book details with <isbn> and <aisle>
    When we execute the AddBook PostAPI Method
    Then Book is successfully added
    Examples:
      | isbn    | aisle |
      | asdfasd | 68977 |
      | rhrrhr  | 67890 |