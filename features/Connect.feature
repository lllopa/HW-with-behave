@tags @Connect
Feature: Connect
    Scenario: Connect to 'localhost': '1234' with 'c:\temp\out.txt' file
        Given Server Address 'localhost'
        And Server port '1234'
        And Output file 'c:\temp\out.txt'
        When Client Starts
        Then Output file should contain some text

    Scenario: Connect to invalid host
        Given Server Address '0.0.0.0'
        And Server port '1234'
        And Output file 'c:\temp\out.txt'
        When Client Starts
        Then [WinError 10049]

    Scenario: Connect to invalid port
        Given Server Address 'localhost'
        And Server port '1111'
        And Output file 'c:\temp\out.txt'
        When Client Starts
        Then [WinError 10061]

    Scenario: Output file is required
        When Client Starts without args
        Then Help message is displayed

    Scenario: Failed test
        Given Server Address 'localhost'
        And Server port '1234'
        And Output file 'c:\tempp\out.txt'
        When Client Starts
        Then [WinError 10061]