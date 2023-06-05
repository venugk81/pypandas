def sendText(str_value):
    print('Printing value:', str_value)

exec ("sendText('hi')")


def click_obj(obj_element, report_step):
    print("Clicking on the element:", report_step)
    sendText(obj_element)

exec ("click_obj('Submit', 'Submit Button')")