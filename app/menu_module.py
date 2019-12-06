import report_module


class Menu:
    
    NOT_VALID_CHOICE_MSG = "\nNot a valid choice. Please try again."
    BLANK_YEAR_MSG = "Year cannot be blank"
    INVALID_MONTH_MSG = ("Invalid month. Please enter a valid month "
                         "from 1 to 12.")
    INVALID_QUARTER_MSG = ("Invalid quarter. Please enter a valid quarter "
                           "from 1 to 4.")
    INVALID_YEAR_MSG = ("Invalid year. Please enter a valid "
                        "year in the format of YYYY.")
    NO_REPORT_MSG = "[ERROR] Report does not exist!"
    QUIT_MSG = "\nGoodbye!"
    
    QUARTER_OR_MONTH_PROMPT = ("Do you want the report by Quarter or Month? "
                               "[Q - Quarterly, M - Monthly]: ")
    YEAR_QUARTER_OR_MONTH_PROMPT = ("Do you want the report by Year, Quarter, "
                                    "or Month? [Y - Year, Q - Quarterly, M - "
                                    "Monthly]: ")
    MONTH_SELECTION_PROMPT = "Which Month? [1 - 12]: "
    QUARTER_SELECTION_PROMPT = "Which Quarter? [1 - 4]: "
    YEAR_SELECTION_PROMPT = "Which Year? [YYYY format]: "
    
    def __init__(self, user):
        self.rp = report_module.Report()
        self.user = user

    def createMenu(self):
        ans = True
        while ans:
            ans = self._menuLoop()
        return ans
    
    
    def _verifyYear(self, year):
        '''
        Check if year has 4 numbers and returns True.
        '''
        if len(str(year)) == 4:
            return True
        else:
            return False
      
    def _menuLoop(self):
        print("\n----------[Main Menu]----------")
        print("" +
              "[1] Dashboard overview\n" +
              "[2] Report Menu\n" +
              "[3] User Administration Menu\n" +
              "")
        menu_selection = input("Please enter an option [1-3, q to Quit] : ")
        if menu_selection == "1":
            self.prompt_for_dashboard_filter()
        elif menu_selection == "2":
            self._report_submenu_loop()
        elif menu_selection == "3":
            self._user_submenu_loop()
        elif menu_selection == "q" or menu_selection == "Q":
            print(self.QUIT_MSG)
            return False
        elif menu_selection == "":
            print(self.NOT_VALID_CHOICE_MSG)
        else:
            print(self.NOT_VALID_CHOICE_MSG)
        return True

    def _user_submenu_loop(self):
        while True:
            print("\n----------[User Administration Menu]----------")
            print("" +
                  "[1] Add New User\n" +
                  "[2] Delete Existing User\n" +
                  "")
            menu_selection = input("Please enter an option [1-2, r to Return "
                                   "to the Main Menu] : ")
            if menu_selection == "1":
                self.user.addNewUser()
            elif menu_selection == "2":
                self.user.deleteuser()
            elif menu_selection == "r" or menu_selection == "R":
                break
            elif menu_selection == "":
                print(self.NOT_VALID_CHOICE_MSG)
            else:
                print(self.NOT_VALID_CHOICE_MSG)

    def _report_submenu_loop(self):
        while True:
            print("\n------------[Report Menu]------------")
            print()
            print("" +
                  "[1] Most Profitable Product Report\n" +
                  "[2] Least Profitable Product Report\n" +
                  "[3] Most Profitable Customer Report\n" +
                  "[4] Least Profitable Customer Report\n\n" +
                  "==========[Report Sub-Menus]==========\n\n"
                  "[5] Profit Analysis Reports menu\n" +
                  "")
            menu_selection = input("Please enter an option [1-5, r to Return "
                                   "to the Main Menu] : ")
            if menu_selection == "1":
                self.prompt_for_report_filter(1)
            elif menu_selection == "2":
                self.prompt_for_report_filter(2)
            elif menu_selection == "3":
                self.prompt_for_report_filter(3)
            elif menu_selection == "4":
                self.prompt_for_report_filter(4)
            elif menu_selection == "5":
                self._report_analysis_submenu()
            elif menu_selection == "r" or menu_selection == "R":
                break
            elif menu_selection == "":
                print(self.NOT_VALID_CHOICE_MSG)
            else:
                print(self.NOT_VALID_CHOICE_MSG)

    def _report_analysis_submenu(self):
        while True:
            print("\n------[Profit Analysis Report Menu]------")
            print()
            print("" +
                  "[1] Sales and Profits by Region\n" +
                  "[2] Discounts Given out by Region\n" +
                  "[3] Discounts by Category and Region\n" +
                  "[4] Top 10 Customers Profits Without Discounts\n" +
                  "[5] Bottom 10 Customer Profits With Discounts\n" +
                  "")
            menu_selection = input("Please enter an option [1-5, r to Return "
                                   "to the Main Menu] : ")
            if menu_selection == "1":
                self.prompt_for_analysis_filter(1)
            elif menu_selection == "2":
                self.prompt_for_analysis_filter(2)
            elif menu_selection == "3":
                self.prompt_for_analysis_filter(3)
            elif menu_selection == "4":
                self.prompt_for_analysis_filter(4)
            elif menu_selection == "5":
                self.prompt_for_analysis_filter(5)
            elif menu_selection == "6":
                self.prompt_for_analysis_filter(6)                
            elif menu_selection == "r" or menu_selection == "R":
                break
            elif menu_selection == "":
                print(self.NOT_VALID_CHOICE_MSG)
            else:
                print(self.NOT_VALID_CHOICE_MSG)

    def prompt_for_dashboard_filter(self):
        report_range, report_type = self.prompt_selection(0)
        
        self.rp.dashboard_report(
                report_range[0], report_range[1], report_range[2], 
                report_range[3], False, report_type, report_range[0])
        self.rp.dashboard_pie_graphs(
                report_range[0], report_range[1], report_range[2], 
                report_range[3], False, report_type, report_range[0])

    def prompt_for_report_filter(self, report_num):
        report_range, report_type = self.prompt_selection(0)

        if report_num == 1:
            self.rp.profit_of_ten_products_ave(
                    report_range[0], report_range[1], report_range[2], 
                    report_range[3], False, report_type, report_range[0])
        elif report_num == 2:
            self.rp.profit_of_ten_products_ave(
                    report_range[0], report_range[1], report_range[2], 
                    report_range[3], True, report_type, report_range[0])
        elif report_num == 3:
            self.rp.active_customer_report(
                    report_range[0], report_range[1], report_range[2], 
                    report_range[3], False, report_type, report_range[0])
        elif report_num == 4:
            self.rp.active_customer_report(
                    report_range[0], report_range[1], report_range[2], 
                    report_range[3], True, report_type, report_range[0])
        elif report_num == 5:
            pass
        elif report_num == 6:
            pass
        else:
            print(self.NO_REPORT_MSG)
            
    def prompt_for_analysis_filter(self, report_num):
        report_range, report_type = self.prompt_selection(1)
         
        if report_num == 1:
            if report_type == 'y' or report_type == 'Y':
                self.rp.sales_and_profits_by_region_yearly(report_range[1])
            else:
                self.rp.sales_and_profits_by_region(
                        report_range[0], report_range[1], report_range[2], 
                        report_range[3], report_type, report_range[0])
        elif report_num == 2:
            self.rp.discounts_by_region(
                    report_range[0], report_range[1], report_range[2], 
                    report_range[3], report_type, report_range[0])
        elif report_num == 3:
            self.rp.discounts_by_category_and_region(
                    report_range[0], report_range[1], report_range[2], 
                    report_range[3], report_type, report_range[0])
        elif report_num == 4:
            self.rp.topcust_no_disc(
                    report_range[0], report_range[1], report_range[2], 
                    report_range[3], report_type, report_range[0])
        elif report_num == 5:
            self.rp.topcust_high_disc(
                    report_range[0], report_range[1], report_range[2], 
                    report_range[3], report_type, report_range[0])
        else:
            print(self.NO_REPORT_MSG)

    def prompt_selection(self, report_selector):
        """
        Method to display prompts.
        report_selector = 0 will display prompt for Quarter or Month
        report_selector = 1 will display prompt for Year, Quarter, or Month
        
        """
        report_range = []
        
        while True:
            if not report_selector == 1:
                report_type = input(self.QUARTER_OR_MONTH_PROMPT)
            else:
                report_type = input(self.YEAR_QUARTER_OR_MONTH_PROMPT)
            
            if report_type == 'q' or report_type == 'Q':
                while True:
                    try:
                        quarter = int(input(self.QUARTER_SELECTION_PROMPT))
                    except:
                        print(self.INVALID_QUARTER_MSG)
                        continue
                    if 1 <= quarter <= 4:
                        break
                    else:
                        print(self.INVALID_QUARTER_MSG)
                        continue
                while True:
                    try:
                        year = int(input(self.YEAR_SELECTION_PROMPT))
                    except:
                        print(self.INVALID_YEAR_MSG)
                        continue
                    if year is None:
                        print(self.BLANK_YEAR_MSG)
                        continue
                    else:
                        while True:
                            if not self._verifyYear(year):
                                print(self.INVALID_YEAR_MSG)
                                try:
                                    year = int(input(
                                               self.YEAR_SELECTION_PROMPT))
                                except:
                                    print(self.INVALID_YEAR_MSG)
                                    continue
                                continue
                            else:
                                report_range = self.quarter_to_months(quarter,
                                                                      year)
                                break
                        break
                break
            elif report_type == 'm' or report_type == 'M':
                while True:
                    try:
                        month = int(input(self.MONTH_SELECTION_PROMPT))
                    except:
                        print(self.INVALID_MONTH_MSG)
                        continue
                    if 1 <= month <= 12:
                        break
                    else:
                        print(self.INVALID_MONTH_MSG)
                        continue
                while True:
                    try:
                        year = int(input(self.YEAR_SELECTION_PROMPT))
                    except:
                        print(self.INVALID_YEAR_MSG)
                        continue
                    if year is None:
                        print(self.BLANK_YEAR_MSG)
                        continue
                    else:
                        while True:
                            if not self._verifyYear(year):
                                print(self.INVALID_YEAR_MSG)
                                try:
                                    year = int(input(
                                               self.YEAR_SELECTION_PROMPT))
                                except:
                                    print(self.INVALID_YEAR_MSG)
                                    continue
                                continue
                            else:
                                report_range.append(month)
                                report_range.append(year)
                                report_range.append(month)
                                report_range.append(year)
                                break
                        break
                break
            elif report_type == 'y' or report_type == 'Y':
                while True:
                    try:
                        year = int(input(self.YEAR_SELECTION_PROMPT))
                    except:
                        print(self.INVALID_YEAR_MSG)
                        continue
                    if year is None:
                        print(self.BLANK_YEAR_MSG)
                        continue
                    else:
                        while True:
                            if not self._verifyYear(year):
                                print(self.INVALID_YEAR_MSG)
                                try:
                                    year = int(input(
                                               self.YEAR_SELECTION_PROMPT))
                                except:
                                    print(self.INVALID_YEAR_MSG)
                                    continue
                                continue
                            else:
                                report_range.append(1)
                                report_range.append(year)
                                report_range.append(12)
                                report_range.append(year)
                                break
                        break
                break
            else:
                print(self.NOT_VALID_CHOICE_MSG)
                
        return report_range, report_type

    def quarter_to_months(self, quarter, year):
        report_range = []
        starting_month = (quarter * 3) - 2
        report_range.append(starting_month)
        report_range.append(year)        
        
        ending_month = quarter * 3
        report_range.append(ending_month)
        report_range.append(year)
        
        return report_range        
