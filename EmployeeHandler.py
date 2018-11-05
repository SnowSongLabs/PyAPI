def EmployeeHandler(employeeID, newDictionary):
    """This is how to handle the employee data structure"""

    # A return key of 1 means failed, a return key of 0 means pass

    employeeFields = ['EmployeeId', 'LastName', 'FirstName', 'Title', 'ReportsTo', 'BirthDate', 'HireDate',
                      'Address', 'City', 'State', 'Country', 'PostalCode', 'Phone', 'Fax', 'Email']

    statusDict = {}

    # Check the params for any incorrect values - if they are found the request will fail and no updates will be made
    for key in newDictionary:
        if (key not in employeeFields):
            statusDict[1] = str("Incorrect field/value in employee update method. Please check your request and try again.\n" \
                   "Error in field:\n\n%s : %s" % (key, newDictionary[key]))

    # All of the keys are valid db field - build the query

    statusDict[0] = str("Passed - todo")

    return statusDict