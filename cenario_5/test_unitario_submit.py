'''
const handleSubmit = (evt) => {
    evt.preventDefault();

    if (!firstName) {
      return setError("First Name is required");
    }

    // Allow to pass for error_user without lastName, as it is impossible to set (errors are thrown)
    if (!lastName && !isErrorUser()) {
      return setError("Last Name is required");
    }

    if (!postalCode) {
      return setError("Postal Code is required");
    }

    // If we're here, we have our required info. Redirect!
    history.push(ROUTES.CHECKOUT_STEP_TWO);

    return "";
  };

'''

import unittest

def handleSubmit(firstname= False,lastname=False,postalcode=False):
    if firstname == False:
        return "Frist Name is required"
    if lastname == False:
        return "Last Name is required"
    if postalcode == False:
        return "Postal code is required"
    return "ok"
    
class TestHandle(unittest.TestCase):
    def test_handle(self):
        self.assertEqual(handleSubmit(),"Frist Name is required")
        self.assertEqual(handleSubmit("pedro"),"Last Name is required")
        self.assertEqual(handleSubmit("pedro", "liu"),"Postal code is required")
        self.assertEqual(handleSubmit("pedro", "liu", 10), "ok")       
        self.assertEqual(handleSubmit("pedro",False,10),"Last Name is required")
    

if __name__ == '__main__':
    unittest.main()

