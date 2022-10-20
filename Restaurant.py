# imports libraries
import sys
import pandas
import unittest

#--end--


#restaurant class
class restaurant:
    #constructor
    def __init__(self,file_path):
        
        """
        Here, file_path of log file is given which is read with pandas library using read_csv() method.
        The data in the file is then saved in DataFrame named : self.restaurant_data
        
        Here, self._check_duplicate_data() function is also run so, to check duplicacy in our log records.
        """

        self.restaurant_data = pandas.read_csv(file_path)
        self._check_duplicate_data()
    

    #Check the data for repated eater_id and foodmenu_id
    def _check_duplicate_data(self):

        duplicate_data = self.restaurant_data[self.restaurant_data.duplicated()]
        
        if len(duplicate_data)>0:
            raise TypeError('Logs file contains Duplicate Records')
            
    
    #This Fuction print the top 3 MENU ITEMS ID's 
    def top3_menuItems(self):
        result = self.restaurant_data['foodmenu_id'].value_counts()[:3].index.tolist()
        return result

    #Print Data of file for testing purpose 
    def print_data(self):
        print(self.restaurant_data)




# Unit Test Casea for Restaurant Functions
class Test_Restaurant(unittest.TestCase):
      
    def setUp(self):
        pass
  
    # This test case show how duplicates raise the error in restaurant class
    def test_with_duplicate(self):

        """
        In this TestCase log_duplicate file is given which will raise the error "Logs file contains Duplicate Records"
        in the Restaurant class function _check_duplicate_data.
        """

        file_path = "log_duplicate.csv"

        with self.assertRaises(Exception) as context:

            logs = restaurant(file_path=file_path)
            result = logs.top3_menuItems()
        
        #print('Error is : ',context.exception)
        self.assertEqual('Logs file contains Duplicate Records',str(context.exception))
    
    def test_without_duplicate(self):

        """
        In this TestCase log_without_duplicate file is given which will not raise any error but will give
        the top 3 foodmenu_id ordererd by the users.
        """

        file_path = "log_without_duplicate.csv"
        logs = restaurant(file_path=file_path)
        result = logs.top3_menuItems()

        self.assertEqual(result,[1,2,3])

  
   
    
if __name__ == '__main__':
    #Run the test cases
    unittest.main()