# AccuKnox Assignment

#Ques 1:
->  Class restaurant is created with parameter file_path of log file which is read with pandas library using read_csv() method.
    The data in the file is then saved in DataFrame named : self.restaurant_data
    In the constructor 'self._check_duplicate_data()' function is also called so, to check duplicacy in our log records.

-> The '_check_duplicate_data()' class method checks the file for duplicates record and if found it raises the
   error : "TypeError('Logs file contains Duplicate Records')".
    
-> In class restaurant 'top3_menuItems' class method returns the list of top 3 MENU ITEMS ID's.

-> After Unit TestCases is written with the help of python unittest.TestCase mpdule.
   
   The name of unittest class is Test_Restaurant.
   In this class two UnitTest cases:
      First test Case test_with_duplicate(self):
        In this TestCase log_duplicate file is given which will raise the error "Logs file contains Duplicate Records"
        in the Restaurant class function _check_duplicate_data.
        
      Second TestCase test_without_duplicate(self):
        In this TestCase log_without_duplicate file is given which will not raise any error but will give
        the top 3 foodmenu_id ordererd by the users.
        
-> At last main function is called in which unittest.main() is called to ran all test cases.
-> Code is written in the file Restaurant.py.
-> Two logs is created for testing named log_without_duplicate and log_with_duplicate.

#Ques 2:
  -> In question Debugging is done in which it is found that Infinite Loop is due to Cyclic Tree formation in the code.
    Code is corrected and the Debug is explained in details in the program : Debug_Tree.py
    
 Written by : Jayant Sharma
