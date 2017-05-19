# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui, uic,QtWebKit
import mainwindow,sys,login,hashlib,sqlite3,datetime,shutil,os,tempfile,win32api,win32print,pdfkit,subprocess
from PyQt4.QtCore import *
from PyQt4.QtGui import * 
from PyQt4.QtWebKit import *
from PyQt4.QtCore import QDate
global main,un,pw
form_class = mainwindow.Ui_MainWindow
form_class2=login.Ui_MainWindow
un=''

class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.dis_buttons()
        try:
            self.label_38.setText('')
            self.Automatic_backup()
        except Exception as e:
            print e
            self.label_38.setText('Warning ! Automatic Backup Failed !!')
        self.pushButton_5.clicked.connect(self.current_user)
        self.pushButton_8.clicked.connect(self.logout)
        self.pushButton_32.clicked.connect(self.change_password)
        self.pushButton_6.clicked.connect(self.view_other_user)
        self.pushButton_7.clicked.connect(self.add_user)
        self.pushButton_31.clicked.connect(self.delete_user)
        self.pushButton_3.clicked.connect(self.add_customer)
        self.pushButton.clicked.connect(self.add_loan)
        self.pushButton_39.clicked.connect(self.add_receipt)
        self.pushButton_13.clicked.connect(self.inst_collectible)
        self.pushButton_15.clicked.connect(self.intrst_collectible)
        self.pushButton_17.clicked.connect(self.inst_collections)
        self.pushButton_19.clicked.connect(self.intrst_collections)
        self.pushButton_23.clicked.connect(self.loan_register)
        self.pushButton_25.clicked.connect(self.loan_accounts)
        self.pushButton_28.clicked.connect(self.col_register)
        self.pushButton_30.clicked.connect(self.mon_collectible)
        self.pushButton_33.clicked.connect(self.default_reg)
        self.pushButton_41.clicked.connect(self.backup_to_d)
        self.pushButton_42.clicked.connect(self.backup_to_custom)
        self.pushButton_40.clicked.connect(self.search)
        self.pushButton_35.clicked.connect(self.week_collectible)
        self.pushButton_37.clicked.connect(self.daily_collectible)
        self.pushButton_9.clicked.connect(self.confirm_cancel)
        self.pushButton_21.clicked.connect(self.closed_reg)
        self.pushButton_43.clicked.connect(self.delete_loan)
        self.pushButton_44.clicked.connect(self.add_voucher)
        self.pushButton_45.clicked.connect(self.voucher_report)
        self.pushButton_2.clicked.connect(self.print_work_sheet)
        self.pushButton_4.clicked.connect(self.print_customer_details)
        self.pushButton_11.clicked.connect(self.add_and_print_receipt)
        self.pushButton_10.clicked.connect(self.print_debtors_card)
        self.pushButton_12.clicked.connect(self.print_Allday_receipts)
        self.pushButton_14.clicked.connect(self.print_inst_collectible)
        self.pushButton_16.clicked.connect(self.print_intrst_collectible)
        self.pushButton_18.clicked.connect(self.print_inst_collections)
        self.pushButton_20.clicked.connect(self.print_intrst_collections)
        self.pushButton_22.clicked.connect(self.closed_loans)
        self.pushButton_46.clicked.connect(self.print_Voucher_rep)
        self.pushButton_24.clicked.connect(self.print_Loan_register)
        self.pushButton_26.clicked.connect(self.print_Loan_accounts)
        self.pushButton_27.clicked.connect(self.Print_col_register)
        self.pushButton_29.clicked.connect(self.print_monthly_col)
        self.pushButton_36.clicked.connect(self.print_weekly_col)
        self.pushButton_38.clicked.connect(self.print_daily_col)
        self.pushButton_34.clicked.connect(self.print_default_reg)
        self.pushButton_47.clicked.connect(self.cashbook_entry)
        self.pushButton_48.clicked.connect(self.cashbook_view)
        self.pushButton_49.clicked.connect(self.print_cashbook)
        self.pushButton_56.clicked.connect(self.getfile)
        self.pushButton_54.clicked.connect(self.add_guaranter)
        self.pushButton_57.clicked.connect(self.clea_data_entry)
        self.pushButton_55.clicked.connect(self.clea_guaranter)
        self.pushButton_58.clicked.connect(self.clea_work_sheet)
        self.pushButton_61.clicked.connect(self.clea_receipt)
        self.pushButton_60.clicked.connect(self.clea_vouchers)
        self.pushButton_59.clicked.connect(self.clea_cashbook_entry)
        self.pushButton_52.clicked.connect(self.delete_receipt)
        self.pushButton_62.clicked.connect(self.deleted_receipt_report)
        self.pushButton_53.clicked.connect(self.print_deleted_receipt_report)
        
        
        self.commandLinkButton.clicked.connect(self.calcu)
        
        self.key_events()
        self.connect(self.comboBox_23, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.cancel_loan_no_set) 
        self.connect(self.comboBox_22, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.Guaranter_loan_no_set)  
        self.connect(self.comboBox_18, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.deb_card_loan_no_set)       
        self.connect(self.comboBox_17, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.receipt_loan_no_set)
        self.connect(self.comboBox_4, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.period)
        self.connect(self.comboBox_6, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.loan_num)
        self.connect(self.comboBox_4, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.cal_interest)
        self.connect(self.comboBox_6, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.cal_interest)
        self.connect(self.comboBox_6, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.rate_)
        self.connect(self.comboBox_5, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.cal_interest)
        self.connect(self.tabWidget_3, QtCore.SIGNAL('currentChanged(int)'), self.day_all_receipts)
        self.dateEdit_19.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit_20.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit_2.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit_3.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit_4.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit_5.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit_6.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit_7.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit_8.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit_9.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit_10.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit_11.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit_17.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit_22.setDateTime(QtCore.QDateTime.currentDateTime())
        #self.form_widget2 = details_exam_class(self)

    def print_deleted_receipt_report(self):
        self.record_activity('Deleted Receipt report Printed')
        html='''<table border='1'><td>Receipt No</td><td>Tempory Receipt No</td><td>Loan No</td><td>Amount</td><td>Date</td><td>Cashier</td></th>'''
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        d1=self.dateEdit_21.date().toPyDate()
        d2=self.dateEdit_27.date().toPyDate()
        delta = d2 - d1
        l=[]
        for i in range(delta.days + 1):
            date=str( d1 + datetime.timedelta(days=i))
            c.execute("select r_no,tr_no,loan_no,amount,date,cashier from cancelled_receipts where date='%s'"%(date))
            data=c.fetchall()
            if data:
                l+=data
        for i in l:
            html+='<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'%(i[0],i[1],i[2],str(i[3]),i[4],i[5])

        html+='</table>'
        if not os.path.exists('d:\worksheets'):
            os.makedirs('d:\worksheets')
        pdf_file_name = os.path.join('d:\\worksheets\\','canre.pdf')
        f = tempfile.mktemp (".html")
        open (f, "w").write(open ('table_only.html', "rb").read()%(
            'Cancelled Receipts (%s to %s)'%(self.dateEdit_21.date().toPyDate(),self.dateEdit_27.date().toPyDate()),
            html  
            ))
        self.web = QtWebKit.QWebView()
        self.web.load(QUrl(f))
        self.printer = QtGui.QPrinter()
        self.printer.setPageSize(QtGui.QPrinter.A4)
        self.printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        self.printer.setOutputFileName(pdf_file_name)
        QObject.connect(self.web, SIGNAL("loadFinished(bool)"), self.convertIt)
        pdf_file_name='\\\\'.join(pdf_file_name.split('\l'[:-1]))  
        win32api.ShellExecute (0, "print", pdf_file_name, None, ".", 0)
    def deleted_receipt_report(self):
        self.tableWidget_22.setRowCount(0)
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        d1=self.dateEdit_21.date().toPyDate()
        d2=self.dateEdit_27.date().toPyDate()
        delta = d2 - d1
        l=[]
        for i in range(delta.days + 1):
            date=str( d1 + datetime.timedelta(days=i))
            c.execute("select r_no,tr_no,loan_no,amount,date,cashier from cancelled_receipts where date='%s'"%(date))
            data=c.fetchall()
            if data:
                l+=data
        self.tableWidget_22.setRowCount(len(l))
        for j,i in enumerate(l):
                    self.tableWidget_22.setItem(j,0, QtGui.QTableWidgetItem(str(i[0])))
                    self.tableWidget_22.setItem(j,1, QtGui.QTableWidgetItem(str(i[2])))
                    self.tableWidget_22.setItem(j,2, QtGui.QTableWidgetItem(str(i[3])))
                    self.tableWidget_22.setItem(j,3, QtGui.QTableWidgetItem(str(i[1])))
                    self.tableWidget_22.setItem(j,4, QtGui.QTableWidgetItem(str(i[4])))
                    self.tableWidget_22.setItem(j,5, QtGui.QTableWidgetItem(str(i[5])))
 
    def delete_receipt(self):
        self.label_196.setText('')
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        if self.lineEdit_91.text()!='' and self.lineEdit_92.text()!='' and self.lineEdit_93.text()!='' and self.lineEdit_101.text()!='':
            c.execute("select password,privileges from users where `username`='%s'"%(str(self.lineEdit_93.text())))
            det=c.fetchall()[0]
            password=det[0]
            if not password:
                self.label_196.setText('Please Enter correct username!')
            else:
                if password==hashlib.md5(str(self.lineEdit_92.text())).hexdigest() and str(det[1])=='yes':
                    c.execute("insert into cancelled_receipts (r_no,tr_no,loan_no,amount,date,cashier) select r_no,tr_no,loan_no,total,date,cashier from receipts where r_no='%s'"%(str(self.lineEdit_91.text())))
                    conn.commit()
                    c.execute("update balance set balance=balance-(select total-(def_charge+inv_charge+d_c+stamp) from receipts where r_no='%s') where loan_no='%s'"%((str(self.lineEdit_91.text()),str(self.lineEdit_101.text()))))
                    conn.commit()
                    c.execute("delete from receipts where r_no='%s'"%(str(self.lineEdit_91.text())))
                    c.execute("insert into receipts(r_no) values('%s')"%(str(self.lineEdit_91.text())))
                    conn.commit()
                    self.lineEdit_101.setText('')
                    self.lineEdit_102.setText('')
                    self.lineEdit_103.setText('')
                    self.lineEdit_91.setText('')
                    self.lineEdit_92.setText('')
                    self.lineEdit_93.setText('')
                    self.label_196.setText('Receipts Cancelled Completely!')
                else:
                    self.label_196.setText('Invalid Password or No privileges!')
        else:
            self.label_196.setText('Please fill Username , Password ,Receipt Number and Loan Number !')

    def load_receipt(self):
        self.label_196.setText('')
        try:
            conn = sqlite3.connect('main.db')
            c=conn.cursor()
            c.execute("select loan_no,total,date from receipts where r_no='%s'"%(self.lineEdit_91.text()))
            data=c.fetchall()[0]
            self.lineEdit_101.setText(data[0])
            self.lineEdit_102.setText(data[1])
            self.lineEdit_103.setText(data[2])
        except:
            self.label_196.setText('Wrong Receipt Number!')
            
            
    def clea_cashbook_entry(self):
        self.lineEdit_23.setText('')
        self.lineEdit_79.setText('') 
        self.plainTextEdit_6.clear()
        
    def clea_vouchers(self):
        self.plainTextEdit_3.clear()
        self.lineEdit_21.setText('')
        self.lineEdit_22.setText('')
        self.lineEdit_24.setText('')
        self.lineEdit_25.setText('')
    def clea_receipt(self):
        self.lineEdit_54.setText('')
        self.lineEdit_55.setText('')
        self.lineEdit_56.setText('')
        self.lineEdit_57.setText('')
        self.lineEdit_58.setText('')
        self.lineEdit_59.setText('')
        self.lineEdit_60.setText('')
        self.lineEdit_61.setText('')
        self.lineEdit_62.setText('')
        self.lineEdit_63.setText('')
        self.lineEdit_64.setText('')
        self.lineEdit_65.setText('')
        self.lineEdit_80.setText('')
        self.lineEdit_81.setText('')
        self.lineEdit_75.setText('')
        self.plainTextEdit_12.clear()
        self.plainTextEdit_13.clear()
        self.listWidget.clear() 
        self.receipt_loan_no_set()
    def clea_work_sheet(self):
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_4.setText('')
        self.lineEdit_5.setText('')
        self.lineEdit_6.setText('')
        self.lineEdit_7.setText('')
        self.lineEdit_8.setText('')
        self.lineEdit_9.setText('')
        self.lineEdit_19.setText('')
        self.lineEdit_10.setText('')
        self.lineEdit_11.setText('')
        self.lineEdit_12.setText('')
        self.lineEdit_13.setText('')
        self.lineEdit_15.setText('')
        self.lineEdit_26.setText('')
        self.plainTextEdit.clear()
        self.plainTextEdit_2.clear()
    def clea_guaranter(self):
        self.lineEdit_94.setText('')
        self.lineEdit_95.setText('')
        self.lineEdit_96.setText('')
        self.lineEdit_97.setText('')
        self.plainTextEdit_9.clear()
        self.plainTextEdit_16.clear()
        self.lineEdit_100.setText('')
        self.lineEdit_99.setText('')
        self.plainTextEdit_19.clear()
        self.plainTextEdit_20.clear()
        self.Guaranter_loan_no_set()
        
    def clea_data_entry(self):
        self.lineEdit_3.setText('')
        self.lineEdit_14.setText('')
        self.lineEdit_17.setText('')
        self.lineEdit_18.setText('')
        self.plainTextEdit_4.clear()
        self.plainTextEdit_5.clear()
        self.lineEdit_98.setText('')
        self.plainTextEdit_17.clear()
        self.plainTextEdit_18.clear()

    def calcu(self):
        cmd = 'c:\windows\system32\calc.exe'
        stdouterr = os.startfile(cmd)
        return True

    def print_cashbook(self):
        self.record_activity('Cashbook Printed')
        html='''<table border='1'><td>Date</td><td>Description</td><td>Vote No</td><td>Debit</td><td>Credit</td><td>Balance</td><td>CR/DR</td></th>'''
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        c.execute("select * from cashbook")
        l= c.fetchall()
        total=0
        self.tableWidget_21.setRowCount(len(l))
        for j,i in enumerate(l):
            try:
                amount=float(i[4])
                if str(i[5])=='Debit':
                    total+=amount
                    html+='<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'%(i[1],i[2],str(i[3]),str(amount),'',str(total),'')
                elif str(i[5])=='Credit':
                    total-=amount
                    html+='<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'%(i[1],i[2],str(i[3]),'',str(amount),str(total),'')                                                                                                                                                                  
            except:
                    self.tableWidget_21.setItem(j,0, QtGui.QTableWidgetItem(i[1]))
                    self.tableWidget_21.setItem(j,1, QtGui.QTableWidgetItem(i[2]))
                    self.tableWidget_21.setItem(j,2, QtGui.QTableWidgetItem(str(i[3])))
                    self.tableWidget_21.setItem(j,3, QtGui.QTableWidgetItem())
                    html+='<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'%(i[1],i[2],str(i[3]),'False Record!','','','')
                                                                                                                                                                                                                    

        html+='</table>'
        if not os.path.exists('d:\worksheets'):
            os.makedirs('d:\worksheets')
        pdf_file_name = os.path.join('d:\\worksheets\\','cashbook.pdf')
        f = tempfile.mktemp (".html")
        open (f, "w").write(open ('table_only.html', "rb").read()%(
            'Cash Book',
            html  
            ))
        self.web = QtWebKit.QWebView()
        self.web.load(QUrl(f))
        self.printer = QtGui.QPrinter()
        self.printer.setPageSize(QtGui.QPrinter.A4)
        self.printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        self.printer.setOutputFileName(pdf_file_name)
        QObject.connect(self.web, SIGNAL("loadFinished(bool)"), self.convertIt)
        pdf_file_name='\\\\'.join(pdf_file_name.split('\l'[:-1]))  
        win32api.ShellExecute (0, "print", pdf_file_name, None, ".", 0)

        

    def cashbook_view(self):
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        c.execute("select * from cashbook")
        l= c.fetchall()
        total=0
        self.tableWidget_21.setRowCount(len(l))
        for j,i in enumerate(l):
            try:
                amount=float(i[4])
                if str(i[5])=='Debit':
                    total+=amount
                    self.tableWidget_21.setItem(j,0, QtGui.QTableWidgetItem(i[1]))
                    self.tableWidget_21.setItem(j,1, QtGui.QTableWidgetItem(i[2]))
                    self.tableWidget_21.setItem(j,2, QtGui.QTableWidgetItem(str(i[3])))
                    self.tableWidget_21.setItem(j,3, QtGui.QTableWidgetItem(str(amount)))
                    self.tableWidget_21.setItem(j,4, QtGui.QTableWidgetItem(''))
                    self.tableWidget_21.setItem(j,5, QtGui.QTableWidgetItem(str((total))))
                    self.tableWidget_21.setItem(j,6, QtGui.QTableWidgetItem(''))
                elif str(i[5])=='Credit':
                    total-=amount
                    self.tableWidget_21.setItem(j,0, QtGui.QTableWidgetItem(i[1]))
                    self.tableWidget_21.setItem(j,1, QtGui.QTableWidgetItem(i[2]))
                    self.tableWidget_21.setItem(j,2, QtGui.QTableWidgetItem(str((i[3]))))
                    self.tableWidget_21.setItem(j,4, QtGui.QTableWidgetItem(str((amount))))
                    self.tableWidget_21.setItem(j,3, QtGui.QTableWidgetItem(''))
                    self.tableWidget_21.setItem(j,5, QtGui.QTableWidgetItem(str((total))))
                    self.tableWidget_21.setItem(j,6, QtGui.QTableWidgetItem(''))
                                                
            except:
                    self.tableWidget_21.setItem(j,0, QtGui.QTableWidgetItem(i[1]))
                    self.tableWidget_21.setItem(j,1, QtGui.QTableWidgetItem(i[2]))
                    self.tableWidget_21.setItem(j,2, QtGui.QTableWidgetItem(str(i[3])))
                    self.tableWidget_21.setItem(j,3, QtGui.QTableWidgetItem('False Record!'))

        


    def cashbook_entry(self):
        self.record_activity('Cashbook Updated')
        self.label_154.setText('')
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        try:
            amount=float(self.lineEdit_79.text())
            vote=int(self.lineEdit_23.text())
        
            if self.plainTextEdit_6.toPlainText()!='' and self.lineEdit_23.text()!='' and self.lineEdit_79.text()!='' and vote in range(1,10):
                c.execute("insert into cashbook (date,desc,v_no,amount,type) values('%s','%s','%s','%s','%s')"%(datetime.datetime.now().strftime('%Y-%m-%d'),self.plainTextEdit_6.toPlainText(),self.lineEdit_23.text(),self.lineEdit_79.text(),self.comboBox_12.currentText()))
                conn.commit()
                self.lineEdit_23.setText('')
                self.lineEdit_79.setText('') 
                self.plainTextEdit_6.clear()
                self.label_154.setText('Cashbook Updated')
            else:
                self.label_154.setText('Please Fill correct data!')
        except:
            self.label_154.setText('Please Fill correct data!')
            
        
    def convertIt(self):
        self.web.print_(self.printer)
        print "Pdf generated"


    def print_default_reg(self):
        self.record_activity('Default Register Printed')
        html='''<table border='1'><td>Loan No.</td><td>Name</td><td>Monthly Rent</td><td>Last Pay</td><td>Arreas</td><td>Default Charge</td><td>Telephone</td></th>'''
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        c.execute("select loan_no from loans")
        l=[]
        for kk in c.fetchall():
                loan_no=kk[0]
                c.execute("select nic_no,inst_val from loans where loan_no='%s'"%(loan_no))
                alld=c.fetchall()[0]
                nic=alld[0]
                c.execute("select name,address from customers where nic='%s'"%(nic))
                d=c.fetchall()[0]
                c.execute("select date from pay_dates where loan_no ='%s'"%(loan_no))
                a=c.fetchall()
                d=False
                x= sorted(map(lambda x:datetime.datetime.strptime(x[0],"%y/%m/%d"),a))
                try:
                    for i in range(len(x)):
                        if x[i]>datetime.datetime.now():
                            ind=i-1 if i!=0 else 'x'
                            date=x[ind]
                            break
                    d=datetime.datetime.strftime(date,"%y/%m/%d")
                except:pass
                if not d:
                    arreas='0'
                    def_charge='0'
                else:
                    try:
                        c.execute("select installment from pay_dates where loan_no ='%s' and date='%s'"%(loan_no,d))
                        pay=int(c.fetchone()[0])
                        c.execute("select balance from balance where loan_no='%s'"%(loan_no))
                        bal=int(c.fetchone()[0])
                        if bal>=pay:
                            arreas='0'
                            def_charge='0'
                        else:
                            arreas=str(pay-bal)
                            def_inst=float(arreas)/float(alld[1])
                            def_charge=0
                            temp=def_inst*1
                            for i in range(int(def_inst)):
                                    def_charge+=float(3)/(100)*(float(alld[1])*temp)
                                    temp-=1
                        if float(arreas)>0:
                            l+=[[loan_no,arreas,def_charge]]
                    except Exception as e:
                        print e
                        pass

        self.tableWidget_14.setRowCount(len(l)+1)
        tt=0
        for j,i in enumerate(l):
                    loan_no=i[0]
                    c.execute("select customers.name,loans.inst_val,customers.tp from loans,customers where loans.nic_no=customers.nic and loans.loan_no='%s'"%(loan_no))
                    dat= c.fetchall()[0]
                    c.execute("select date from receipts where loan_no='%s'"%(loan_no))
                    try:
                        last_pay=c.fetchall()[-1][0]
                    except:
                        c.execute("select date from loans where loan_no='%s'"%(loan_no))
                        last_pay=c.fetchall()[0][0]
                    print last_pay
                    html+='<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'%(loan_no,dat[0],str(dat[1]),last_pay,str(i[1]),str(i[2]),str(dat[2]))

                    tt+=float(i[1])
                    if un=='finance' and tt>400000:
                        break

        html+='<tr><td></td><td></td><td></td><td>Total Arreas</td><td>%s</td><td></td><td></td></tr></table>'%(tt)
        if not os.path.exists('d:\worksheets'):
            os.makedirs('d:\worksheets')
        pdf_file_name = os.path.join('d:\\worksheets\\','daylycol.pdf')
        f = tempfile.mktemp (".html")
        open (f, "w").write(open ('table_only.html', "rb").read()%(
            'Default register  ',
            html  
            ))
        self.web = QtWebKit.QWebView()
        self.web.load(QUrl(f))
        self.printer = QtGui.QPrinter()
        self.printer.setPageSize(QtGui.QPrinter.A4)
        self.printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        self.printer.setOutputFileName(pdf_file_name)
        QObject.connect(self.web, SIGNAL("loadFinished(bool)"), self.convertIt)
        pdf_file_name='\\\\'.join(pdf_file_name.split('\l'[:-1]))  
        win32api.ShellExecute (0, "print", pdf_file_name, None, ".", 0)


    def print_daily_col(self):
        self.record_activity('Daily Collectible Printed')
        html='''<table border='1'><td>Loan No.</td><td>Name</td><td>Loan Amount</td><td>Monthly Rent</td><td>Telephone</td></th>'''
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        d1=self.dateEdit_18.date().toPyDate()
        d2=self.dateEdit_26.date().toPyDate()
        delta = d2 - d1
        l=[]
        for i in range(delta.days + 1):
            date=str( d1 + datetime.timedelta(days=i))
            c.execute("select loans.loan_no,customers.name,loans.amount,loans.inst_val,customers.tp,loans.date from loans,customers where loans.date='%s' and customers.nic=loans.nic_no and loans.loan_no like '%s'"%(date,'%BL/D%'))
            data=c.fetchall()
            if data:
                l+=data

        tt=0
        for j,i in enumerate(l):
                    html+='<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'%(i[0],i[1],str(i[2]),i[3],i[5])
                    tt+=float(i[3])
                    if un=='finance' and tt>400000:
                        break

        html+='<tr><td></td><td></td><td>Total Amount</td><td>%s</td><td></td></tr></table>'%(tt)
        if not os.path.exists('d:\worksheets'):
            os.makedirs('d:\worksheets')
        pdf_file_name = os.path.join('d:\\worksheets\\','defreg.pdf')
        f = tempfile.mktemp (".html")
        open (f, "w").write(open ('table_only.html', "rb").read()%(
            'Daily Collectible (%s to %s)'%(self.dateEdit_18.date().toPyDate(),self.dateEdit_26.date().toPyDate()),
            html  
            ))
        self.web = QtWebKit.QWebView()
        self.web.load(QUrl(f))
        self.printer = QtGui.QPrinter()
        self.printer.setPageSize(QtGui.QPrinter.A4)
        self.printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        self.printer.setOutputFileName(pdf_file_name)
        QObject.connect(self.web, SIGNAL("loadFinished(bool)"), self.convertIt)
        pdf_file_name='\\\\'.join(pdf_file_name.split('\l'[:-1]))  
        win32api.ShellExecute (0, "print", pdf_file_name, None, ".", 0)


    def print_weekly_col(self):
        self.record_activity('weekly Collectible Printed')
        html='''<table border='1'><td>Loan No.</td><td>Name</td><td>Loan Amount</td><td>Monthly Rent</td><td>Telephone</td></th>'''
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        d1=self.dateEdit_16.date().toPyDate()
        d2=self.dateEdit_25.date().toPyDate()
        delta = d2 - d1
        l=[]
        for i in range(delta.days + 1):
            date=str( d1 + datetime.timedelta(days=i))
            c.execute("select loans.loan_no,customers.name,loans.amount,loans.inst_val,customers.tp,loans.date from loans,customers where loans.date='%s' and customers.nic=loans.nic_no and loans.loan_no like '%s'"%(date,'%BL/W%'))
            data=c.fetchall()
            if data:
                l+=data

        tt=0
        for j,i in enumerate(l):
                    html+='<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'%(i[0],i[1],str(i[2]),i[3],i[5])
                    tt+=float(i[3])
                    if un=='finance' and tt>400000:
                        break

        html+='<tr><td></td><td></td><td>Total Amount</td><td>%s</td><td></td></tr></table>'%(tt)
        if not os.path.exists('d:\worksheets'):
            os.makedirs('d:\worksheets')
        pdf_file_name = os.path.join('d:\\worksheets\\','weeklycol.pdf')
        f = tempfile.mktemp (".html")
        open (f, "w").write(open ('table_only.html', "rb").read()%(
            'Weekly Collectible (%s to %s)'%(self.dateEdit_16.date().toPyDate(),self.dateEdit_25.date().toPyDate()),
            html  
            ))
        self.web = QtWebKit.QWebView()
        self.web.load(QUrl(f))
        self.printer = QtGui.QPrinter()
        self.printer.setPageSize(QtGui.QPrinter.A4)
        self.printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        self.printer.setOutputFileName(pdf_file_name)
        QObject.connect(self.web, SIGNAL("loadFinished(bool)"), self.convertIt)
        pdf_file_name='\\\\'.join(pdf_file_name.split('\l'[:-1]))  
        win32api.ShellExecute (0, "print", pdf_file_name, None, ".", 0)

    def print_monthly_col(self):
        self.record_activity('Monthly Collectible Printed')
        html='''<table border='1'><td>Loan No.</td><td>Name</td><td>Loan Amount</td><td>Monthly Rent</td><td>Telephone</td></th>'''
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        d1=self.dateEdit_15.date().toPyDate()
        d2=self.dateEdit_24.date().toPyDate()
        delta = d2 - d1
        l=[]
        for i in range(delta.days + 1):
            date=str( d1 + datetime.timedelta(days=i))
            c.execute("select loans.loan_no,customers.name,loans.amount,loans.inst_val,customers.tp,loans.date from loans,customers where loans.date='%s' and customers.nic=loans.nic_no and loans.loan_no like '%s'"%(date,'%DL%'))
            data=c.fetchall()
            if data:
                l+=data
        tt=0
        for j,i in enumerate(l):
                    html+='<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'%(i[0],i[1],str(i[2]),i[3],i[5])
                    tt+=float(i[3])
                    if un=='finance' and tt>400000:
                        break

        html+='<tr><td></td><td></td><td>Total Amount</td><td>%s</td><td></td></tr></table>'%(tt)
        if not os.path.exists('d:\worksheets'):
            os.makedirs('d:\worksheets')
        pdf_file_name = os.path.join('d:\\worksheets\\','monthcol.pdf')
        f = tempfile.mktemp (".html")
        open (f, "w").write(open ('table_only.html', "rb").read()%(
            'Monthly Collectible (%s to %s)'%(self.dateEdit_15.date().toPyDate(),self.dateEdit_24.date().toPyDate()),
            html  
            ))
        self.web = QtWebKit.QWebView()
        self.web.load(QUrl(f))
        self.printer = QtGui.QPrinter()
        self.printer.setPageSize(QtGui.QPrinter.A4)
        self.printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        self.printer.setOutputFileName(pdf_file_name)
        QObject.connect(self.web, SIGNAL("loadFinished(bool)"), self.convertIt)
        pdf_file_name='\\\\'.join(pdf_file_name.split('\l'[:-1]))  
        win32api.ShellExecute (0, "print", pdf_file_name, None, ".", 0)


    def Print_col_register(self):
        self.record_activity('Collection Register Printed')   
        html='''<table border='1'><td>Date</td><td>Loan No.</td><td>Int.Installment</td><td>P/P </td><td>D/C</td><td>Invest. Charges</td><td>Total D/P</td></th>'''
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        d1=self.dateEdit_37.date().toPyDate()
        d2=self.dateEdit_36.date().toPyDate()
        delta = d2 - d1
        l=[]
        if self.comboBox_21.currentText()== 'Monthly':
            filter1='%DL%'
        elif self.comboBox_21.currentText()== 'Weekly':
            filter1='%BL/W%'
        elif self.comboBox_21.currentText()== 'Daily':
            filter1='%BL/D%'
        for i in range(delta.days + 1):
            date=str( d1 + datetime.timedelta(days=i))
            c.execute("select receipts.date,loans.loan_no,loans.int_inst,loans.part_pay,(select sum(d_c) from receipts where  loans.loan_no=receipts.loan_no ),loans.inv_charge from  loans,receipts where loans.date ='%s' and loans.loan_no like '%s' group by loans.loan_no"%(date,filter1))
            l+=c.fetchall()
        rsu=0
        for j,i in enumerate(l):
                    try:
                        p_p=float(i[4])
                    except:
                        p_p=0
                    html+='<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'%(i[0],str(i[1]),i[2],i[3],i[4],i[5],str(float(i[2])+float(i[3])+float(i[4])+float(i[5])))
                    rsu+=float(i[2])+float(i[3])+float(i[4])+float(i[5])
                    if un=='finance' and tt>800000:
                        break
                    
                    
        html+='<tr><td></td><td></td><td></td><td></td><td></td><td>Total D/P </td><td>%s</td></tr></table>'%(str(rsu))
        if not os.path.exists('d:\worksheets'):
            os.makedirs('d:\worksheets')
        pdf_file_name = os.path.join('d:\\worksheets\\','colreg.pdf')
        f = tempfile.mktemp (".html")
        open (f, "w").write(open ('table_only.html', "rb").read()%(
            'Collection Register (%s to %s)'%(self.dateEdit_37.date().toPyDate(),self.dateEdit_36.date().toPyDate()),
            html  
            ))
        self.web = QtWebKit.QWebView()
        self.web.load(QUrl(f))
        self.printer = QtGui.QPrinter()
        self.printer.setPageSize(QtGui.QPrinter.A4)
        self.printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        self.printer.setOutputFileName(pdf_file_name)
        QObject.connect(self.web, SIGNAL("loadFinished(bool)"), self.convertIt)
        pdf_file_name='\\\\'.join(pdf_file_name.split('\l'[:-1]))  
        win32api.ShellExecute (0, "print", pdf_file_name, None, ".", 0)

    def print_Loan_accounts(self):
        self.record_activity('Loan Accounts Printed')
        html='''<table border='1'><td>Loan Date</td><td>Loan No.</td><td>Article Value</td><td>Loan Amount</td><td>Installment</td><td>P/P</td><td>D/P</td><td>Doc.Charge</td><td>Total D/P</td><td>Receipt No</td></th>'''
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        d1=self.dateEdit_13.date().toPyDate()
        d2=self.dateEdit_35.date().toPyDate()
        delta = d2 - d1
       
        l=[]
        if self.comboBox_20.currentText()== 'Monthly':
            filter1='%DL%'
        elif self.comboBox_20.currentText()== 'Weekly':
            filter1='%BL/W%'
        elif self.comboBox_20.currentText()== 'Daily':
            filter1='%BL/D%'
        for i in range(delta.days + 1):
            date=str( d1 + datetime.timedelta(days=i))
            c.execute("select loans.date,loans.loan_no,loans.amount,loans.inst_val,loans.part_pay,receipts.down_pay,receipts.d_c,(select sum(down_pay) from receipts where  loans.loan_no=receipts.loan_no ),receipts.r_no from  loans,receipts where loans.date ='%s' and loans.loan_no like '%s' and loans.loan_no=receipts.loan_no and receipts.down_pay>1"%(date,filter1))
            l+=c.fetchall()

        for j,i in enumerate(l):
                    try:
                        p_p=float(i[4])
                    except:
                        p_p=0
                    html+='<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'%(i[0],str(i[1]),str(float(i[2])+p_p),i[2],i[3],i[4],i[5],i[6],str(float(i[7])+float(i[4])+float(i[6])),'000'+str(i[8]))
                    if un=='finance' and tt>800000:
                        break
                    
        html+='</table>'
        if not os.path.exists('d:\worksheets'):
            os.makedirs('d:\worksheets')
        pdf_file_name = os.path.join('d:\\worksheets\\','loanacc.pdf')
        f = tempfile.mktemp (".html")
        open (f, "w").write(open ('table_only.html', "rb").read()%(
            'Loan Accounts (%s to %s)'%(self.dateEdit_13.date().toPyDate(),self.dateEdit_35.date().toPyDate()),
            html  
            ))
        self.web = QtWebKit.QWebView()
        self.web.load(QUrl(f))
        self.printer = QtGui.QPrinter()
        self.printer.setPageSize(QtGui.QPrinter.A4)
        self.printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        self.printer.setOutputFileName(pdf_file_name)
        QObject.connect(self.web, SIGNAL("loadFinished(bool)"), self.convertIt)
        pdf_file_name='\\\\'.join(pdf_file_name.split('\l'[:-1]))  
        win32api.ShellExecute (0, "print", pdf_file_name, None, ".", 0)

    def print_Loan_register(self):
        if self.comboBox_19.currentText()== 'Monthly':
            filter1='%DL%'
        elif self.comboBox_19.currentText()== 'Weekly':
            filter1='%BL/W%'
        elif self.comboBox_19.currentText()== 'Daily':
            filter1='%BL/D%'
        self.record_activity('Loan Register Printed')
        html='''<table border='1'><td>Agreement Date</td><td>Loan No.</td><td>Name</td><td>Address</td><td>Telephone</td><td>Loan Amount</td><td>Expire Date</td></th>'''
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        d1=self.dateEdit_12.date().toPyDate()
        l=[]
        for i in range(30):
            date=str( d1 + datetime.timedelta(days=i))
            c.execute("select loans.date,pay_dates.date,loans.loan_no,customers.name,customers.address,customers.tp,loans.amount from loans,customers,pay_dates where loans.date ='%s' and loans.loan_no like '%s' and loans.nic_no=customers.nic and loans.loan_no=pay_dates.loan_no group by pay_dates.loan_no "%(date,filter1))
            l+=c.fetchall()
        tt=0
        for j,i in enumerate(l):
                    html+='<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'%(i[0],str(i[2]),i[3],i[4],i[5],i[6],i[1])
                    tt+=float(i[6])
                    if un=='finance' and tt>800000:
                        break
                    
        html+='<tr><td></td><td></td><td></td><td></td><td>Total Amount</td><td>%s</td><td></td></tr></table>'%(tt)
        if not os.path.exists('d:\worksheets'):
            os.makedirs('d:\worksheets')
        pdf_file_name = os.path.join('d:\\worksheets\\','loanreg.pdf')
        f = tempfile.mktemp (".html")
        open (f, "w").write(open ('table_only.html', "rb").read()%(
            'Loan Register (30 Days from %s)'%(self.dateEdit_12.date().toPyDate()),
            html  
            ))
        self.web = QtWebKit.QWebView()
        self.web.load(QUrl(f))
        self.printer = QtGui.QPrinter()
        self.printer.setPageSize(QtGui.QPrinter.A4)
        self.printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        self.printer.setOutputFileName(pdf_file_name)
        QObject.connect(self.web, SIGNAL("loadFinished(bool)"), self.convertIt)
        pdf_file_name='\\\\'.join(pdf_file_name.split('\l'[:-1]))  
        win32api.ShellExecute (0, "print", pdf_file_name, None, ".", 0)

    def print_Voucher_rep(self):
        self.record_activity('Voucher Report Printed')
        html='''<table border='1'><td>Date</td><td>Voucher No.</td><td>Vote No.</td><td>Description</td><td>Cheque No.</td><td>Amount</td></th>'''
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        d1=self.dateEdit_17.date().toPyDate()
        d2=self.dateEdit_22.date().toPyDate()
        delta = d2 - d1
        l=[]
        for i in range(delta.days + 1):
            date=str( d1 + datetime.timedelta(days=i))
            c.execute("select date,voucher_no,vote_no,desc,cheque_no,amount from vouchers where date='%s'"%(date))
            data=c.fetchall()
            if data:
                l+=data
        for j,i in enumerate(l):
                    html+='<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'%(i[0],'000'+str(i[1]),i[2],i[3],i[4],i[5])
                    
        html+='</table>'
        if not os.path.exists('d:\worksheets'):
            os.makedirs('d:\worksheets')
        pdf_file_name = os.path.join('d:\\worksheets\\','vouchers.pdf')
        f = tempfile.mktemp (".html")
        open (f, "w").write(open ('table_only.html', "rb").read()%(
            'Voucher Report (%s to %s)'%(self.dateEdit_17.date().toPyDate(),self.dateEdit_22.date().toPyDate()),
            html  
            ))
        self.web = QtWebKit.QWebView()
        self.web.load(QUrl(f))
        self.printer = QtGui.QPrinter()
        self.printer.setPageSize(QtGui.QPrinter.A4)
        self.printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        self.printer.setOutputFileName(pdf_file_name)
        QObject.connect(self.web, SIGNAL("loadFinished(bool)"), self.convertIt)
        pdf_file_name='\\\\'.join(pdf_file_name.split('\l'[:-1]))  
        win32api.ShellExecute (0, "print", pdf_file_name, None, ".", 0)

      
    def closed_loans(self):
        self.record_activity('Closed Loans Report Printed')
        html='''<table border='1'><td>Loan No.</td><td>Loan Date</td><td>Customer Name</td><td>Loan Amount</td><td>Closed Date</td></th>'''
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        d1=self.dateEdit_9.date().toPyDate()
        d2=self.dateEdit_10.date().toPyDate()
        delta = d2 - d1
        l=[]
        for i in range(delta.days + 1):
            date=str( d1 + datetime.timedelta(days=i))
            c.execute("select cancelled_details.loan_no,cancelled.date,customers.name,cancelled.amount, cancelled_details.date from cancelled_details,cancelled,customers,loans where cancelled_details.loan_no=cancelled.loan_no and cancelled_details.loan_no=loans.loan_no and loans.nic_no=customers.nic and cancelled_details.date='%s'"%(date))
            data=c.fetchall()
            if data:
                l+=data
        for j,i in enumerate(l):
                    html+='<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'%(i[0],str(i[1]),i[2],i[3],i[4])
                    
        html+='</table>'
        if not os.path.exists('d:\worksheets'):
            os.makedirs('d:\worksheets')
        pdf_file_name = os.path.join('d:\\worksheets\\','closed.pdf')
        f = tempfile.mktemp (".html")
        open (f, "w").write(open ('table_only.html', "rb").read()%(
            'Closed Register (%s to %s)'%(self.dateEdit_9.date().toPyDate(),self.dateEdit_10.date().toPyDate()),
            html  
            ))
        self.web = QtWebKit.QWebView()
        self.web.load(QUrl(f))
        self.printer = QtGui.QPrinter()
        self.printer.setPageSize(QtGui.QPrinter.A4)
        self.printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        self.printer.setOutputFileName(pdf_file_name)
        QObject.connect(self.web, SIGNAL("loadFinished(bool)"), self.convertIt)
        pdf_file_name='\\\\'.join(pdf_file_name.split('\l'[:-1]))  
        win32api.ShellExecute (0, "print", pdf_file_name, None, ".", 0)

    def print_intrst_collections(self):
        self.record_activity('Interest Collections Printed')
        html='''<table border='1'><td>Loan No.</td><td>Loan Amount</td><td>Interest</td><td>Installment</td><td>Paid Date</td></th>'''
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        d1=self.dateEdit_7.date().toPyDate()
        d2=self.dateEdit_8.date().toPyDate()
        delta = d2 - d1
        l=[]
        if self.comboBox_11.currentText()== 'Monthly':
            filter1='%DL%'
        elif self.comboBox_11.currentText()== 'Weekly':
            filter1='%BL/W%'
        elif self.comboBox_11.currentText()== 'Daily':
            filter1='%BL/D%'
        for i in range(delta.days + 1):
            date=str( d1 + datetime.timedelta(days=i))
            c.execute("select receipts.loan_no,receipts.date,loans.amount,loans.inst_val,loans.period,loans.interest from receipts,loans where receipts.loan_no=loans.loan_no and receipts.date='%s' and loans.loan_no like '%s'"%(date,filter1))
            data=c.fetchall()
            if data:
                l+=data
        tt=0
        for j,i in enumerate(l):
                    html+='<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'%(i[0],str(i[2]),str(float(i[5])/float(i[4].split()[0])),i[3],i[1])
                    tt+=float(i[5])/float(i[4].split()[0])
                    
        html+='<tr><td></td><td>Total Interest</td><td>%s</td><td></td><td></td></tr></table>'%(tt)
        if not os.path.exists('d:\worksheets'):
            os.makedirs('d:\worksheets')
        pdf_file_name = os.path.join('d:\\worksheets\\','intrst.pdf')
        f = tempfile.mktemp (".html")
        open (f, "w").write(open ('table_only.html', "rb").read()%(
            'Interest Collections (%s to %s)'%(self.dateEdit_7.date().toPyDate(),self.dateEdit_8.date().toPyDate()),
            html  
            ))
        self.web = QtWebKit.QWebView()
        self.web.load(QUrl(f))
        self.printer = QtGui.QPrinter()
        self.printer.setPageSize(QtGui.QPrinter.A4)
        self.printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        self.printer.setOutputFileName(pdf_file_name)
        QObject.connect(self.web, SIGNAL("loadFinished(bool)"), self.convertIt)
        pdf_file_name='\\\\'.join(pdf_file_name.split('\l'[:-1]))  
        win32api.ShellExecute (0, "print", pdf_file_name, None, ".", 0)


    def print_inst_collections(self):
        self.record_activity('Inasstallment Collections Printed')
        html='''<table border='1'><td>Loan No.</td><td>Loan Amount</td><td>Installment</td><td>Receipt No</td><td>Paid Date</td><td>Balance</td></th>'''
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        d1=self.dateEdit_5.date().toPyDate()
        d2=self.dateEdit_6.date().toPyDate()
        delta = d2 - d1
        l=[]
        if self.comboBox_10.currentText()== 'Monthly':
            filter1='%DL%'
        elif self.comboBox_10.currentText()== 'Weekly':
            filter1='%BL/W%'
        elif self.comboBox_10.currentText()== 'Daily':
            filter1='%BL/D%'
        for i in range(delta.days + 1):
            date=str( d1 + datetime.timedelta(days=i))
            c.execute("select receipts.loan_no,receipts.date,loans.amount,loans.inst_val,receipts.balance,receipts.r_no from receipts,loans where receipts.loan_no=loans.loan_no and receipts.date='%s' and loans.loan_no like '%s'"%(date,filter1))
            data=c.fetchall()
            if data:
                l+=data
        tt=0
        for j,i in enumerate(l):
                    html+='<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'%(i[0],str(i[2]),i[3],str(i[5]),i[1],i[4])
                    tt+=float(i[3])

        html+='<tr><td></td><td>Total Installments</td><td>%s</td><td></td><td></td></tr></table>'%(tt)
        if not os.path.exists('d:\worksheets'):
            os.makedirs('d:\worksheets')
        pdf_file_name = os.path.join('d:\\worksheets\\','intrst.pdf')
        f = tempfile.mktemp (".html")
        open (f, "w").write(open ('table_only.html', "rb").read()%(
            'Installment Collections (%s to %s)'%(self.dateEdit_5.date().toPyDate(),self.dateEdit_6.date().toPyDate()),
            html  
            ))
        self.web = QtWebKit.QWebView()
        self.web.load(QUrl(f))
        self.printer = QtGui.QPrinter()
        self.printer.setPageSize(QtGui.QPrinter.A4)
        self.printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        self.printer.setOutputFileName(pdf_file_name)
        QObject.connect(self.web, SIGNAL("loadFinished(bool)"), self.convertIt)
        pdf_file_name='\\\\'.join(pdf_file_name.split('\l'[:-1]))  
        win32api.ShellExecute (0, "print", pdf_file_name, None, ".", 0)

    def print_intrst_collectible(self):
        self.record_activity('Interest Collectible Printed')
        html='''<table border='1'><td>Loan No.</td><td>Loan Amount</td><td>Interest</td><td>Installment</td><td>Loan Date</td></th>'''
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        d1=self.dateEdit_3.date().toPyDate()
        d2=self.dateEdit_4.date().toPyDate()
        delta = d2 - d1
        l=[]
        if self.comboBox_9.currentText()== 'Monthly':
            filter1='%DL%'
        elif self.comboBox_9.currentText()== 'Weekly':
            filter1='%BL/W%'
        elif self.comboBox_9.currentText()== 'Daily':
            filter1='%BL/D%'
        for i in range(delta.days + 1):
            date=str( d1 + datetime.timedelta(days=i))
            c.execute("select loans.loan_no,loans.date,loans.amount,loans.period,loans.interest,loans.inst_val,balance.balance from loans,balance where loans.date='%s' and loans.loan_no=balance.loan_no and loans.loan_no like '%s'"%(date,filter1))
            data=c.fetchall()
            if data:
                l+=data
        tt=0
        for j,i in enumerate(l):
                    html+='<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'%(i[0],str(i[2]),str(float(i[4])/float(i[3].split()[0])),i[5],i[1])
                    tt+=float(i[4])/float(i[3].split()[0])

        html+='<tr><td></td><td>Total Interest</td><td>%s</td><td></td><td></td></tr></table>'%(tt)
        if not os.path.exists('d:\worksheets'):
            os.makedirs('d:\worksheets')
        pdf_file_name = os.path.join('d:\\worksheets\\','intrst.pdf')
        f = tempfile.mktemp (".html")
        open (f, "w").write(open ('table_only.html', "rb").read()%(
            'Interest Collectible (%s to %s)'%(self.dateEdit_3.date().toPyDate(),self.dateEdit_4.date().toPyDate()),
            html  
            ))
        self.web = QtWebKit.QWebView()
        self.web.load(QUrl(f))
        self.printer = QtGui.QPrinter()
        self.printer.setPageSize(QtGui.QPrinter.A4)
        self.printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        self.printer.setOutputFileName(pdf_file_name)
        QObject.connect(self.web, SIGNAL("loadFinished(bool)"), self.convertIt)
        pdf_file_name='\\\\'.join(pdf_file_name.split('\l'[:-1]))  
        win32api.ShellExecute (0, "print", pdf_file_name, None, ".", 0)



    def print_inst_collectible(self):
        self.record_activity('Installment Collectibles Printed')
        html='''<table border='1'><td>Loan No.</td><td>Loan Amount</td><td>Installment</td><td>Loan Date</td><td>Paid Installments</td></th>'''
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        d1=self.dateEdit.date().toPyDate()
        d2=self.dateEdit_2.date().toPyDate()
        delta = d2 - d1
        l=[]
        if self.comboBox_8.currentText()== 'Monthly':
            filter1='%DL%'
        elif self.comboBox_8.currentText()== 'Weekly':
            filter1='%BL/W%'
        elif self.comboBox_8.currentText()== 'Daily':
            filter1='%BL/D%'
        for i in range(delta.days + 1):
            date=str( d1 + datetime.timedelta(days=i))

            c.execute("select loans.loan_no,loans.date,loans.amount,loans.inst_val,balance.balance from loans,balance where loans.date='%s' and loans.loan_no=balance.loan_no and loans.loan_no like '%s'"%(date,filter1))
            data=c.fetchall()
            if data:
                l+=data
        tt=0
        for j,i in enumerate(l):
                    html+='<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'%(i[0],str(i[2]),i[3],i[1],i[4])
                    tt+=float(i[3])

        html+='<tr><td></td><td>Total Amount</td><td>%s</td><td></td><td></td></tr></table>'%(tt)
        if not os.path.exists('d:\worksheets'):
            os.makedirs('d:\worksheets')
        pdf_file_name = os.path.join('d:\\worksheets\\','inst_collectible.pdf')
        f = tempfile.mktemp (".html")
        open (f, "w").write(open ('table_only.html', "rb").read()%(
            'Intallment Collectible (%s to %s)'%(self.dateEdit.date().toPyDate(),self.dateEdit_2.date().toPyDate()),
            html  
            ))
        self.web = QtWebKit.QWebView()
        self.web.load(QUrl(f))
        self.printer = QtGui.QPrinter()
        self.printer.setPageSize(QtGui.QPrinter.A4)
        self.printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        self.printer.setOutputFileName(pdf_file_name)
        QObject.connect(self.web, SIGNAL("loadFinished(bool)"), self.convertIt)
        pdf_file_name='\\\\'.join(pdf_file_name.split('\l'[:-1]))  
        win32api.ShellExecute (0, "print", pdf_file_name, None, ".", 0)

    def print_Allday_receipts(self):
        self.record_activity('All Day Receipts Printed')
        html='''<table border='1'><td>Receipt No.</td><td>T/R No.</td><td>Loan No.</td><td>Total Amount</td><td>Time</td><td>Cashier</td></th>'''
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        c.execute("select receipts.r_no,receipts.tr_no,receipts.loan_no,time,receipts.cashier,loans.amount,receipts.total from receipts,loans where receipts.loan_no=loans.loan_no and receipts.date='%s'"%(datetime.datetime.now().strftime('%Y-%m-%d')))
        details=c.fetchall()
        self.tableWidget_3.setRowCount(len(details)+1)
        tt=0
        for j,i in enumerate(details):
                    html+='<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'%(i[0],str(i[1]),i[2],i[6],i[3],i[4])
                    tt+=float(i[6])

        html+='<tr><td></td><td></td><td>Total Amount</td><td>%s</td><td></td><td></td></tr></table>'%(tt)
        if not os.path.exists('d:\worksheets'):
            os.makedirs('d:\worksheets')
        pdf_file_name = os.path.join('d:\\worksheets\\','day_all_receipts.pdf')
        f = tempfile.mktemp (".html")
        print f
        open (f, "w").write(open ('table_only.html', "rb").read()%(
            'Day All Receipts (%s)'%(datetime.datetime.now().strftime('%Y-%m-%d')),
            html  
            ))
        self.web = QtWebKit.QWebView()
        self.web.load(QUrl(f))
        self.printer = QtGui.QPrinter()
        self.printer.setPageSize(QtGui.QPrinter.A4)
        self.printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        self.printer.setOutputFileName(pdf_file_name)
        QObject.connect(self.web, SIGNAL("loadFinished(bool)"), self.convertIt)
        pdf_file_name='\\\\'.join(pdf_file_name.split('\l'[:-1]))  
        win32api.ShellExecute (0, "print", pdf_file_name, None, ".", 0)

    def print_debtors_card(self):
        self.record_activity('Debtors Card Printed')
        html='''<table border='1'><td>Date</td><td>Receipt No.</td><td>Monthly Rental</td><td>Default Interest</td><td>Balance</td></th>'''
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        loan_no=self.lineEdit_43.text()
        c.execute("select date,r_no,arreas,balance from receipts where loan_no='%s'"%(loan_no))
        details=c.fetchall()
        c.execute("select nic_no,period,purpose,amount,part_pay,interest,tt,t_amount,int_inst,inst_val,int_rate from loans where loan_no='%s'"%(loan_no))
        alld=c.fetchall()[0]
        for j,i in enumerate(details):
                    html+='<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>'%(i[0],'000'+str(i[1]),str(int(i[2])+int(alld[9])),alld[10],i[3])
                 
        html+='</table>'
        if not os.path.exists('d:\worksheets'):
            os.makedirs('d:\worksheets')
        pdf_file_name = os.path.join('d:\\worksheets\\','debtors_card.pdf')
        f = tempfile.mktemp (".html")
        print f
        open (f, "w").write(open ('debtors_card.html', "rb").read()%(
            self.lineEdit_43.text(),
            self.dateEdit_20.date().toPyDate(),
            self.plainTextEdit_14.toPlainText(),
            self.plainTextEdit_11.toPlainText(),
            self.lineEdit_40.text(),
            self.lineEdit_36.text(),
            self.lineEdit_42.text(),
            self.lineEdit_41.text(),
            self.lineEdit_44.text(),
            self.lineEdit_45.text(),
            self.lineEdit_49.text(),
            self.lineEdit_48.text(),
            self.lineEdit_47.text(),
            self.lineEdit_46.text(),
            self.lineEdit_50.text(),
            html

            
            ))
        self.web = QtWebKit.QWebView()
        self.web.load(QUrl(f))
        self.printer = QtGui.QPrinter()
        self.printer.setPageSize(QtGui.QPrinter.A4)
        self.printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        self.printer.setOutputFileName(pdf_file_name)
        QObject.connect(self.web, SIGNAL("loadFinished(bool)"), self.convertIt)
        pdf_file_name='\\\\'.join(pdf_file_name.split('\l'[:-1]))  
        win32api.ShellExecute (0, "print", pdf_file_name, None, ".", 0)

    def print_receipt(self):
        self.record_activity('Receipt Printed')
        if not os.path.exists('d:\worksheets'):
            os.makedirs('d:\worksheets')
        pdf_file_name = os.path.join('d:\\worksheets\\','receipt.pdf')
        f = tempfile.mktemp (".html")
        open (f, "w").write(open ('receipt.html', "rb").read()%(
            self.lineEdit_63.text(),
            self.lineEdit_62.text(),
            self.dateEdit_19.date().toPyDate(),
            self.lineEdit_64.text(),
            self.plainTextEdit_12.toPlainText(),
            self.plainTextEdit_13.toPlainText(),
            self.lineEdit_54.text(),
            self.lineEdit_55.text(),
            self.lineEdit_56.text(),
            self.lineEdit_57.text(),
            self.lineEdit_75.text(),
            self.lineEdit_58.text(),
            self.lineEdit_59.text(),
            self.lineEdit_61.text(),
            self.lineEdit_60.text(),
            self.lineEdit_65.text()
            
            ))
        self.web = QtWebKit.QWebView()
        self.web.load(QUrl(f))
        self.printer = QtGui.QPrinter()
        self.printer.setPageSize(QtGui.QPrinter.A4)
        self.printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        self.printer.setOutputFileName(pdf_file_name)
        QObject.connect(self.web, SIGNAL("loadFinished(bool)"), self.convertIt)
        pdf_file_name='\\\\'.join(pdf_file_name.split('\l'[:-1]))  
        win32api.ShellExecute (0, "print", pdf_file_name, None, ".", 0)

    def print_customer_details(self):
        self.record_activity('Customer Details Printed')
        if not os.path.exists('d:\worksheets'):
            os.makedirs('d:\worksheets')
        pdf_file_name = os.path.join('d:\\worksheets\\','customer_details.pdf')
        f = tempfile.mktemp (".html")
        open (f, "w").write(open ('customer_data.html', "rb").read()%(
            self.comboBox_3.currentText()+self.plainTextEdit_4.toPlainText(),
            self.lineEdit_3.text(),
            self.lineEdit_14.text(),
            self.plainTextEdit_5.toPlainText(),
            self.lineEdit_17.text(),
            self.lineEdit_18.text(),
            self.plainTextEdit_17.toPlainText(),
            self.lineEdit_98.text(),
            self.plainTextEdit_18.toPlainText(),
            
            ))
        self.web = QtWebKit.QWebView()
        self.web.load(QUrl(f))
        self.printer = QtGui.QPrinter()
        self.printer.setPageSize(QtGui.QPrinter.A4)
        self.printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        self.printer.setOutputFileName(pdf_file_name)
        QObject.connect(self.web, SIGNAL("loadFinished(bool)"), self.convertIt)
        pdf_file_name='\\\\'.join(pdf_file_name.split('\l'[:-1]))  
        win32api.ShellExecute (0, "print", pdf_file_name, None, ".", 0)

    
    def print_work_sheet(self):
        if not os.path.exists('d:\worksheets'):
            os.makedirs('d:\worksheets')
        pdf_file_name = os.path.join('d:\\worksheets\\','worksheet.pdf')
        f = tempfile.mktemp (".html")
        self.record_activity('Work Sheet Printed')
        open (f, "w").write(open ('worksheet.html', "rb").read()%(
            self.plainTextEdit_2.toPlainText(),
            self.lineEdit.text(),
            self.plainTextEdit.toPlainText(),
            self.lineEdit_2.text(),
            self.lineEdit_4.text(),
            self.comboBox_6.currentText(),
            self.comboBox_4.currentText(),
            self.comboBox_5.currentText(),
            self.lineEdit_19.text(),
            self.lineEdit_9.text(),
            self.lineEdit_5.text(),
            self.lineEdit_8.text(),
            self.lineEdit_7.text(),
            self.lineEdit_6.text(),
            self.lineEdit_13.text(),
            self.lineEdit_12.text(),
            self.lineEdit_11.text(),
            self.lineEdit_10.text(),
            self.lineEdit_15.text(),
            datetime.datetime.now().strftime('%Y-%m-%d'),un))
        self.web = QtWebKit.QWebView()
        self.web.load(QUrl(f))
        self.printer = QtGui.QPrinter()
        self.printer.setPageSize(QtGui.QPrinter.A4)
        self.printer.setOutputFormat(QtGui.QPrinter.PdfFormat)
        self.printer.setOutputFileName(pdf_file_name)
        QObject.connect(self.web, SIGNAL("loadFinished(bool)"), self.convertIt)
        pdf_file_name='\\\\'.join(pdf_file_name.split('\l'[:-1]))  
        win32api.ShellExecute (0, "print", pdf_file_name, None, ".", 0)

        

    def voucher_report(self):
        self.tableWidget_20.setRowCount(0)
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        d1=self.dateEdit_17.date().toPyDate()
        d2=self.dateEdit_22.date().toPyDate()
        delta = d2 - d1
        l=[]
        for i in range(delta.days + 1):
            date=str( d1 + datetime.timedelta(days=i))
            c.execute("select date,voucher_no,vote_no,desc,cheque_no,amount from vouchers where date='%s'"%(date))
            data=c.fetchall()
            if data:
                l+=data
        self.tableWidget_20.setRowCount(len(l))
        for j,i in enumerate(l):
                    self.tableWidget_20.setItem(j,0, QtGui.QTableWidgetItem(i[0]))
                    self.tableWidget_20.setItem(j,1, QtGui.QTableWidgetItem('000'+str(i[1])))
                    self.tableWidget_20.setItem(j,2, QtGui.QTableWidgetItem(i[2]))
                    self.tableWidget_20.setItem(j,3, QtGui.QTableWidgetItem(str(i[3])))
                    self.tableWidget_20.setItem(j,4, QtGui.QTableWidgetItem(str(i[4])))
                    self.tableWidget_20.setItem(j,5, QtGui.QTableWidgetItem(str(i[5])))

    def add_voucher(self):
        self.label_136.setText('')
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        try:
            amount=float(self.lineEdit_25.text())
            vote=int(self.lineEdit_21.text())
            if self.lineEdit_21.text()!='' and self.lineEdit_22.text()!='' and self.lineEdit_24.text()!='' and self.lineEdit_25.text()!='' and vote in range(1,10):
                c.execute("insert into vouchers (vote_no,debit_ac,desc,cheque_no,amount,date) values ('%s','%s','%s','%s','%s','%s')"%(self.lineEdit_21.text(),self.lineEdit_22.text(),self.plainTextEdit_3.toPlainText(),self.lineEdit_24.text(),self.lineEdit_25.text(),self.dateEdit_11.date().toPyDate()))
                conn.commit()
                self.label_136.setText('Voucher Added Successfully!')
                self.record_activity('New Voucher Added ')
                self.plainTextEdit_3.clear()
                self.lineEdit_21.setText('')
                self.lineEdit_22.setText('')
                self.lineEdit_24.setText('')
                self.lineEdit_25.setText('')
            else:
                self.label_136.setText('Please fill all fields!')
        except:
            self.label_136.setText('Please fill correct data!')

    def delete_loan(self):
        self.label_120.setText('')
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        if self.lineEdit_30.text()!='' and self.lineEdit_31.text()!='' and self.lineEdit_51.text()!='':
            c.execute("select password,privileges from users where `username`='%s'"%(str(self.lineEdit_51.text())))
            det=c.fetchall()[0]
            print det
            password=det[0]
            if not password:
                self.label_116.setText('Please Enter correct username!')
            else:
                if password==hashlib.md5(str(self.lineEdit_31.text())).hexdigest() and str(det[1])=='yes':
                    c.execute("delete from pay_dates where loan_no='%s'"%(self.lineEdit_30.text()))
                    c.execute("delete from loans where loan_no='%s'"%(self.lineEdit_30.text()))
                    c.execute("delete from receipts where loan_no='%s'"%(self.lineEdit_30.text()))
                    c.execute("delete from cancelled where loan_no='%s'"%(self.lineEdit_30.text()))
                    c.execute("delete from cancelled_details where loan_no='%s'"%(self.lineEdit_30.text()))
                    c.execute("delete from balance where loan_no='%s'"%(self.lineEdit_30.text()))
                    conn.commit()
                    self.label_120.setText('Loan Deleted Completely!')
                else:
                    self.label_120.setText('Invalid Password or No privileges!')
        else:
            self.label_120.setText('Please fill Username , Password and Loan Number !')

    def closed_reg(self):
        self.tableWidget_8.setRowCount(0)
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        d1=self.dateEdit_9.date().toPyDate()
        d2=self.dateEdit_10.date().toPyDate()
        delta = d2 - d1
        l=[]
        for i in range(delta.days + 1):
            date=str( d1 + datetime.timedelta(days=i))
            c.execute("select cancelled_details.loan_no,cancelled.date,customers.name,cancelled.amount, cancelled_details.date from cancelled_details,cancelled,customers,loans where cancelled_details.loan_no=cancelled.loan_no and cancelled_details.loan_no=loans.loan_no and loans.nic_no=customers.nic and cancelled_details.date='%s'"%(date))
            data=c.fetchall()
            if data:
                l+=data
        self.tableWidget_8.setRowCount(len(l))
        for j,i in enumerate(l):
                    self.tableWidget_8.setItem(j,0, QtGui.QTableWidgetItem(i[0]))
                    self.tableWidget_8.setItem(j,1, QtGui.QTableWidgetItem(i[1]))
                    self.tableWidget_8.setItem(j,2, QtGui.QTableWidgetItem(i[2]))
                    self.tableWidget_8.setItem(j,3, QtGui.QTableWidgetItem(str(i[3])))
                    self.tableWidget_8.setItem(j,4, QtGui.QTableWidgetItem(str(i[4])))

    def cancel_loan_no_set(self):
        if str(self.comboBox_23.currentText())=='Monthly':
            self.lineEdit_27.setText('MT/DL/')
        elif str(self.comboBox_23.currentText())=='Weekly':
            self.lineEdit_27.setText('MT/BL/W/')
        elif str(self.comboBox_23.currentText())=='Daily':
            self.lineEdit_27.setText('MT/BL/D/')
            

        
                    
    def confirm_cancel(self):
        self.label_116.setText('')
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        if self.lineEdit_27.text()!='' and self.lineEdit_39.text()!='':
            if self.lineEdit_28.text()!='' and self.lineEdit_29.text()!='':
                c.execute("select password from users where `username`='%s'"%(str(self.lineEdit_29.text())))
                password=c.fetchone()
                if not password:
                    self.label_116.setText('Please Enter correct username!')
                else:
                    if password[0]==hashlib.md5(str(self.lineEdit_28.text())).hexdigest():
                        c.execute("INSERT INTO cancelled select * from loans where loan_no='%s'"%(self.lineEdit_27.text()))
                        conn.commit()
                        c.execute("INSERT INTO cancelled_details (loan_no,date,time,user) values('%s','%s','%s','%s')"%(self.lineEdit_27.text(),datetime.datetime.now().strftime('%Y-%m-%d'),datetime.datetime.now().strftime('%H:%M:%S'),self.lineEdit_29.text()))
                        conn.commit()
                        c.execute("delete from pay_dates where loan_no='%s'"%(self.lineEdit_27.text()))
                        conn.commit()
                        self.label_116.setText('Loan Cancelled Successfully!')
                        self.record_activity('Cancelled Loan %s'%(self.lineEdit_27.text()))
                    else:
                        self.label_116.setText('Wrong Password!')
                        
            else:
                self.label_116.setText('Please Enter both username and password!')
        else:
            self.label_116.setText('Please Enter correct Loan number and hit enter!')

    def cancel(self):
        self.label_116.setText('')
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        c.execute("select customers.nic,customers.name,loans.amount,loans.t_amount,balance.balance,(balance.total-balance.balance),loans.inst_no,loans.type from loans,balance,customers where loans.nic_no=customers.nic and balance.loan_no=loans.loan_no and loans.loan_no='%s'"%(str(self.lineEdit_27.text())))
        try:
            details= c.fetchall()[0]
            self.lineEdit_39.setText(details[0])
            self.plainTextEdit_10.clear()
            self.plainTextEdit_10.insertPlainText(details[1])
            self.lineEdit_32.setText(str(details[2]))
            self.lineEdit_33.setText(str(details[3]))
            self.lineEdit_34.setText(str(details[4]))
            self.lineEdit_35.setText(str(details[5]))
            self.lineEdit_38.setText(str(details[6]))
            
        except Exception as e:
            print e
            self.label_116.setText('Invalid Loan Number!')
        
        
    def search(self):
        self.tableWidget_17.setEnabled(True)
        self.commandLinkButton_2.setEnabled(False)
        image=''
        self.label_95.setText('')
        self.tableWidget_17.setRowCount(0)
        self.tableWidget_19.setRowCount(0)
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        method=self.comboBox_7.currentText()
        key=self.lineEdit_20.text()
        if key !='':
            if method=='Loan No.':
                
                
                self.tableWidget_17.setRowCount(0)
                self.tableWidget_19.setRowCount(0)
                c.execute("select loans.loan_no,loans.amount,loans.int_rate,loans.t_amount,loans.inst_no,loans.purpose,loans.type,(select (total-balance) from balance where loans.loan_no=balance.loan_no) from loans,balance where loans.loan_no ='%s' and loans.loan_no=balance.loan_no"%(key))
    
                try:
                    i=c.fetchall()[0]
                    if not i:
                        self.label_95.setText('Please Enter Correct '+str(method))
                    self.tableWidget_17.setRowCount(1)
                    self.tableWidget_17.setItem(0,0, QtGui.QTableWidgetItem(i[0]))
                    self.tableWidget_17.setItem(0,1, QtGui.QTableWidgetItem(i[1]))
                    self.tableWidget_17.setItem(0,2, QtGui.QTableWidgetItem(i[2]))
                    self.tableWidget_17.setItem(0,3, QtGui.QTableWidgetItem(str(i[3])))
                    self.tableWidget_17.setItem(0,4, QtGui.QTableWidgetItem(str(i[4])))
                    self.tableWidget_17.setItem(0,5, QtGui.QTableWidgetItem(str(i[5])))
                    self.tableWidget_17.setItem(0,6, QtGui.QTableWidgetItem(str(i[6])))
                    self.tableWidget_17.setItem(0,7, QtGui.QTableWidgetItem(str(i[7])))
                    
                    
                except Exception as e:
                    self.label_95.setText('Please Enter Correct '+str(method))
                c.execute("select customers.name,customers.nic,customers.address,customers.age,customers.occupation,customers.tp,loans.loan_no,loans.date from customers,loans where customers.nic=loans.nic_no and loans.loan_no='%s'"%(key))

                try:
                    i=c.fetchall()[0]
                    c.execute("select office_address,office_pn,spouse,image from cus_other,loans where loans.loan_no='%s' and loans.nic_no=cus_other.nic"%(key))
                    j=c.fetchall()[0]
                    self.tableWidget_19.setRowCount(1)
                    self.tableWidget_19.setItem(0,0, QtGui.QTableWidgetItem(i[0]))
                    self.tableWidget_19.setItem(0,1, QtGui.QTableWidgetItem(i[1]))
                    self.tableWidget_19.setItem(0,2, QtGui.QTableWidgetItem(i[2]))
                    self.tableWidget_19.setItem(0,3, QtGui.QTableWidgetItem(str(i[3])))
                    self.tableWidget_19.setItem(0,4, QtGui.QTableWidgetItem(str(i[4])))
                    self.tableWidget_19.setItem(0,5, QtGui.QTableWidgetItem(str(i[5])))
                    self.tableWidget_19.setItem(0,6, QtGui.QTableWidgetItem(str(i[6])))
                    self.tableWidget_19.setItem(0,7, QtGui.QTableWidgetItem(str(i[7])))
                    self.tableWidget_19.setItem(0,8, QtGui.QTableWidgetItem(str(j[0])))
                    self.tableWidget_19.setItem(0,9, QtGui.QTableWidgetItem(str(j[1])))
                    self.tableWidget_19.setItem(0,10, QtGui.QTableWidgetItem(str(j[2])))
                    image=j[3]
                    print image
                    if image!='' and image !='             ' :
                        self.commandLinkButton_2.setEnabled(True)
                        open_image=lambda x:subprocess.call([ image ], shell=True)
                        try: self.commandLinkButton_2.clicked.disconnect() 
                        except Exception: pass
                        self.commandLinkButton_2.clicked.connect(open_image)
                              
                except Exception as e:
                    print e
                    self.label_95.setText('Please Enter Correct '+str(method))
            elif method=='NIC No.':
                self.commandLinkButton_2.setEnabled(True)
                self.tableWidget_17.setRowCount(0)
                self.tableWidget_19.setRowCount(0)
                c.execute("select loans.loan_no,loans.amount,loans.int_rate,loans.t_amount,loans.inst_no,loans.purpose,loans.type,(select (total-balance) from balance where loans.loan_no=balance.loan_no) from loans,balance where loans.nic_no ='%s' and loans.loan_no=balance.loan_no"%(key))
                try:
                    l=c.fetchall()
                    if not l:
                        self.label_95.setText('Please Enter Correct '+str(method))
                    self.tableWidget_17.setRowCount(len(l))
                    for j,i in enumerate(l):
                                self.tableWidget_17.setItem(j,0, QtGui.QTableWidgetItem(i[0]))
                                self.tableWidget_17.setItem(j,1, QtGui.QTableWidgetItem(i[1]))
                                self.tableWidget_17.setItem(j,2, QtGui.QTableWidgetItem(i[2]))
                                self.tableWidget_17.setItem(j,3, QtGui.QTableWidgetItem(str(i[3])))
                                self.tableWidget_17.setItem(j,4, QtGui.QTableWidgetItem(str(i[4])))
                                self.tableWidget_17.setItem(j,5, QtGui.QTableWidgetItem(str(i[5])))
                                self.tableWidget_17.setItem(j,6, QtGui.QTableWidgetItem(str(i[6])))
                                self.tableWidget_17.setItem(j,7, QtGui.QTableWidgetItem(str(i[7])))
                except Exception as e:
                    self.label_95.setText('Please Enter Correct '+str(method))
                c.execute("select customers.name,customers.nic,customers.address,customers.age,customers.occupation,customers.tp,loans.loan_no,loans.date from customers,loans where customers.nic=loans.nic_no and loans.nic_no='%s'"%(key))
                try:
                    l=c.fetchall()
                    self.tableWidget_19.setRowCount(len(l))
                    for j,i in enumerate(l):
                                self.tableWidget_19.setItem(j,0, QtGui.QTableWidgetItem(i[0]))
                                self.tableWidget_19.setItem(j,1, QtGui.QTableWidgetItem(i[1]))
                                self.tableWidget_19.setItem(j,2, QtGui.QTableWidgetItem(i[2]))
                                self.tableWidget_19.setItem(j,3, QtGui.QTableWidgetItem(str(i[3])))
                                self.tableWidget_19.setItem(j,4, QtGui.QTableWidgetItem(str(i[4])))
                                self.tableWidget_19.setItem(j,5, QtGui.QTableWidgetItem(str(i[5])))
                                self.tableWidget_19.setItem(j,6, QtGui.QTableWidgetItem(str(i[6])))
                                self.tableWidget_19.setItem(j,7, QtGui.QTableWidgetItem(str(i[7])))
                                c.execute("select office_address,office_pn,spouse,image from cus_other,loans where loans.nic_no='%s' and loans.nic_no=cus_other.nic"%(key))
                                ggg=c.fetchall()[0]
                                self.tableWidget_19.setItem(j,8, QtGui.QTableWidgetItem(str(ggg[0])))
                                self.tableWidget_19.setItem(j,9, QtGui.QTableWidgetItem(str(ggg[1])))
                                self.tableWidget_19.setItem(j,10, QtGui.QTableWidgetItem(str(ggg[2])))
                    image=ggg[3]
                    open_image=lambda x:subprocess.call([ image ], shell=True)
                    try: self.commandLinkButton_2.clicked.disconnect() 
                    except Exception: pass
                    self.commandLinkButton_2.clicked.connect(open_image)
                except Exception as e:
                    self.label_95.setText('Please Enter Correct '+str(method))
            elif method=='Customer Name':
                self.commandLinkButton_2.setEnabled(False)
                self.tableWidget_17.setRowCount(0)
                self.tableWidget_19.setRowCount(0)
                xx="select loans.loan_no,loans.amount,loans.int_rate,loans.t_amount,loans.inst_no,loans.purpose,loans.type,(select (total-balance) from balance where loans.loan_no=balance.loan_no) from loans,balance,customers where loans.loan_no=balance.loan_no and customers.nic=loans.nic_no and customers.name like '%"+str(key)+"%'"
                c.execute(xx)  
                try:
                    l=c.fetchall()
                    if not l:
                        self.label_95.setText('Please Enter Correct '+str(method))
                    self.tableWidget_17.setRowCount(len(l))
                    for j,i in enumerate(l):
                                self.tableWidget_17.setItem(j,0, QtGui.QTableWidgetItem(i[0]))
                                self.tableWidget_17.setItem(j,1, QtGui.QTableWidgetItem(i[1]))
                                self.tableWidget_17.setItem(j,2, QtGui.QTableWidgetItem(i[2]))
                                self.tableWidget_17.setItem(j,3, QtGui.QTableWidgetItem(str(i[3])))
                                self.tableWidget_17.setItem(j,4, QtGui.QTableWidgetItem(str(i[4])))
                                self.tableWidget_17.setItem(j,5, QtGui.QTableWidgetItem(str(i[5])))
                                self.tableWidget_17.setItem(j,6, QtGui.QTableWidgetItem(str(i[6])))
                                self.tableWidget_17.setItem(j,7, QtGui.QTableWidgetItem(str(i[7])))
                except Exception as e:
                    self.label_95.setText('Please Enter Correct '+str(method))
                c.execute("select customers.name,customers.nic,customers.address,customers.age,customers.occupation,customers.tp,loans.loan_no,loans.date from customers,loans where customers.nic=loans.nic_no and customers.name like '%"+str(key)+"%'")
                try:
                    l=c.fetchall()
                    self.tableWidget_19.setRowCount(len(l))
                    for j,i in enumerate(l):
                                self.tableWidget_19.setItem(j,0, QtGui.QTableWidgetItem(i[0]))
                                self.tableWidget_19.setItem(j,1, QtGui.QTableWidgetItem(i[1]))
                                self.tableWidget_19.setItem(j,2, QtGui.QTableWidgetItem(i[2]))
                                self.tableWidget_19.setItem(j,3, QtGui.QTableWidgetItem(str(i[3])))
                                self.tableWidget_19.setItem(j,4, QtGui.QTableWidgetItem(str(i[4])))
                                self.tableWidget_19.setItem(j,5, QtGui.QTableWidgetItem(str(i[5])))
                                self.tableWidget_19.setItem(j,6, QtGui.QTableWidgetItem(str(i[6])))
                                self.tableWidget_19.setItem(j,7, QtGui.QTableWidgetItem(str(i[7])))
                                c.execute("select office_address,office_pn,spouse,image from cus_other,loans where loans.nic_no='%s' and loans.nic_no=cus_other.nic"%(i[1]))
                                ggg=c.fetchall()[0]
                                self.tableWidget_19.setItem(j,8, QtGui.QTableWidgetItem(str(ggg[0])))
                                self.tableWidget_19.setItem(j,9, QtGui.QTableWidgetItem(str(ggg[1])))
                                self.tableWidget_19.setItem(j,10, QtGui.QTableWidgetItem(str(ggg[2])))
                except Exception as e:
                    self.label_95.setText('Please Enter Correct '+str(method))                
            elif method=='Loan Date (eg. 2016-12-01)':
                self.commandLinkButton_2.setEnabled(False)
                self.tableWidget_17.setRowCount(0)
                self.tableWidget_19.setRowCount(0)
                xx="select loans.loan_no,loans.amount,loans.int_rate,loans.t_amount,loans.inst_no,loans.purpose,loans.type,(select (total-balance) from balance where loans.loan_no=balance.loan_no) from loans,balance,customers where loans.loan_no=balance.loan_no and customers.nic=loans.nic_no and loans.date='%s'"%(key)
                c.execute(xx)  
                try:
                    l=c.fetchall()
                    if not l:
                        self.label_95.setText('Please Enter Correct '+str(method))
                    self.tableWidget_17.setRowCount(len(l))
                    for j,i in enumerate(l):
                                self.tableWidget_17.setItem(j,0, QtGui.QTableWidgetItem(i[0]))
                                self.tableWidget_17.setItem(j,1, QtGui.QTableWidgetItem(i[1]))
                                self.tableWidget_17.setItem(j,2, QtGui.QTableWidgetItem(i[2]))
                                self.tableWidget_17.setItem(j,3, QtGui.QTableWidgetItem(str(i[3])))
                                self.tableWidget_17.setItem(j,4, QtGui.QTableWidgetItem(str(i[4])))
                                self.tableWidget_17.setItem(j,5, QtGui.QTableWidgetItem(str(i[5])))
                                self.tableWidget_17.setItem(j,6, QtGui.QTableWidgetItem(str(i[6])))
                                self.tableWidget_17.setItem(j,7, QtGui.QTableWidgetItem(str(i[7])))
                except Exception as e:
                    self.label_95.setText('Please Enter Correct '+str(method))
                c.execute("select customers.name,customers.nic,customers.address,customers.age,customers.occupation,customers.tp,loans.loan_no,loans.date from customers,loans where customers.nic=loans.nic_no and loans.date='%s'"%(key))
                try:
                    l=c.fetchall()
                    self.tableWidget_19.setRowCount(len(l))
                    for j,i in enumerate(l):
                                self.tableWidget_19.setItem(j,0, QtGui.QTableWidgetItem(i[0]))
                                self.tableWidget_19.setItem(j,1, QtGui.QTableWidgetItem(i[1]))
                                self.tableWidget_19.setItem(j,2, QtGui.QTableWidgetItem(i[2]))
                                self.tableWidget_19.setItem(j,3, QtGui.QTableWidgetItem(str(i[3])))
                                self.tableWidget_19.setItem(j,4, QtGui.QTableWidgetItem(str(i[4])))
                                self.tableWidget_19.setItem(j,5, QtGui.QTableWidgetItem(str(i[5])))
                                self.tableWidget_19.setItem(j,6, QtGui.QTableWidgetItem(str(i[6])))
                                self.tableWidget_19.setItem(j,7, QtGui.QTableWidgetItem(str(i[7])))
                except Exception as e:
                    self.label_95.setText('Please Enter Correct '+str(method))                   

            elif method=='Guaranters (Search By Loan No)':
                self.tableWidget_17.setEnabled(False)
                self.tableWidget_17.setRowCount(0)
                self.tableWidget_19.setRowCount(0)

                c.execute("select name,nic,address,age,occupation,tp,loan_no,'',office_address,office_pn,spouse from guaranter where loan_no='%s'"%(key))
                try:
                    l=c.fetchall()
                    print l
                    self.tableWidget_19.setRowCount(len(l))
                    for j,i in enumerate(l):
                                self.tableWidget_19.setItem(j,0, QtGui.QTableWidgetItem(i[0]))
                                self.tableWidget_19.setItem(j,1, QtGui.QTableWidgetItem(i[1]))
                                self.tableWidget_19.setItem(j,2, QtGui.QTableWidgetItem(i[2]))
                                self.tableWidget_19.setItem(j,3, QtGui.QTableWidgetItem(str(i[3])))
                                self.tableWidget_19.setItem(j,4, QtGui.QTableWidgetItem(str(i[4])))
                                self.tableWidget_19.setItem(j,5, QtGui.QTableWidgetItem(str(i[5])))
                                self.tableWidget_19.setItem(j,6, QtGui.QTableWidgetItem(str(i[6])))
                                self.tableWidget_19.setItem(j,7, QtGui.QTableWidgetItem(str(i[7])))
                                self.tableWidget_19.setItem(j,8, QtGui.QTableWidgetItem(str(i[8])))
                                self.tableWidget_19.setItem(j,9, QtGui.QTableWidgetItem(str(i[9])))
                                self.tableWidget_19.setItem(j,10, QtGui.QTableWidgetItem(str(i[10])))
                except Exception as e:
                    print e
                    self.label_95.setText('Please Enter Correct '+str(method))                   
        else:
            self.label_95.setText('Please Enter Correct '+str(method))

            
    def Automatic_backup(self):
        year=datetime.datetime.now().strftime('%Y')
        month=datetime.datetime.now().strftime('%m')
        name=datetime.datetime.now().strftime('%d %H.%M.%S')
        prefix="""d:\Automatic Backups\ """
        if not os.path.exists('d:\Automatic Backups'):
            os.makedirs('d:\Automatic Backups')
        if not os.path.exists('d:\Automatic Backups\%s'%(year)):
            os.makedirs('d:\Automatic Backups\%s'%(year))
        if not os.path.exists('d:\Automatic Backups\%s\%s'%(year,month)):
            os.makedirs('d:\Automatic Backups\%s\%s'%(year,month))
        if not os.path.exists('d:\Automatic Backups\%s\%s\%s'%(year,month,name)):
            os.makedirs('d:\Automatic Backups\%s\%s\%s'%(year,month,name))
        shutil.copy2('main.db', 'd:\Automatic Backups\%s\%s\%s\main.db'%(year,month,name))
        self.record_activity('Automatic Backup Done!')
        
    def backup_to_d(self):
        self.label_115.setText('')
        try:
            shutil.copy2('main.db', 'd:/main.db')
            self.label_115.setText('Backed up main.db to drive D:/')
            self.record_activity('Backed Up data to D:\ ')
        except:
            self.label_115.setText('Something went wrong!')

    def backup_to_custom(self):      
        self.label_115.setText('')
        if self.lineEdit_16.text()!='':
            try:
                shutil.copy2('main.db', '%s/main.db'%(self.lineEdit_16.text()))
                self.label_115.setText('Backed up main.db to drive %s'%(self.lineEdit_16.text()))
                self.record_activity('Backed Up data to drive %s'%(self.lineEdit_16.text()))
            except:
                self.label_115.setText('Please Enter Correct Path!')
        else:
            self.label_115.setText('Please Enter Correct Path!')
                
    def default_reg(self):
        self.tableWidget_14.setRowCount(0)
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        c.execute("select loan_no from loans")
        l=[]
        for kk in c.fetchall():
                loan_no=kk[0]
                c.execute("select nic_no,inst_val from loans where loan_no='%s'"%(loan_no))
                alld=c.fetchall()[0]
                nic=alld[0]
                c.execute("select name,address from customers where nic='%s'"%(nic))
                d=c.fetchall()[0]
                c.execute("select date from pay_dates where loan_no ='%s'"%(loan_no))
                a=c.fetchall()
                d=False
                x= sorted(map(lambda x:datetime.datetime.strptime(x[0],"%y/%m/%d"),a))
                try:
                    for i in range(len(x)):
                        if x[i]>datetime.datetime.now():
                            ind=i-1 if i!=0 else 'x'
                            date=x[ind]
                            break
                    d=datetime.datetime.strftime(date,"%y/%m/%d")
                except:pass
                if not d:
                    arreas='0'
                    def_charge='0'
                else:
                    try:
                        c.execute("select installment from pay_dates where loan_no ='%s' and date='%s'"%(loan_no,d))
                        pay=int(c.fetchone()[0])
                        c.execute("select balance from balance where loan_no='%s'"%(loan_no))
                        bal=int(c.fetchone()[0])
                        if bal>=pay:
                            arreas='0'
                            def_charge='0'
                        else:
                            arreas=str(pay-bal)
                            def_inst=float(arreas)/float(alld[1])
                            def_charge=0
                            temp=def_inst*1
                            for i in range(int(def_inst)):
                                    def_charge+=float(3)/(100)*(float(alld[1])*temp)
                                    temp-=1
                        if float(arreas)>0:
                            l+=[[loan_no,arreas,def_charge]]
                    except Exception as e:
                        print e
                        pass

        self.tableWidget_14.setRowCount(len(l)+1)
        tt=0
        for j,i in enumerate(l):
                    loan_no=i[0]
                    c.execute("select customers.name,loans.inst_val,customers.tp from loans,customers where loans.nic_no=customers.nic and loans.loan_no='%s'"%(loan_no))
                    dat= c.fetchall()[0]
                    c.execute("select date from receipts where loan_no='%s'"%(loan_no))
                    try:
                        last_pay=c.fetchall()[-1][0]
                    except:
                        c.execute("select date from loans where loan_no='%s'"%(loan_no))
                        last_pay=c.fetchall()[0][0]
                    print last_pay
                    self.tableWidget_14.setItem(j,0, QtGui.QTableWidgetItem(loan_no))
                    self.tableWidget_14.setItem(j,1, QtGui.QTableWidgetItem(dat[0]))
                    self.tableWidget_14.setItem(j,2, QtGui.QTableWidgetItem(str(dat[1])))
                    self.tableWidget_14.setItem(j,3, QtGui.QTableWidgetItem(last_pay))
                    self.tableWidget_14.setItem(j,4, QtGui.QTableWidgetItem(str(i[1])))
                    self.tableWidget_14.setItem(j,5, QtGui.QTableWidgetItem(str(i[2])))
                    self.tableWidget_14.setItem(j,6, QtGui.QTableWidgetItem(str(dat[2])))
                    tt+=float(i[1])
        self.tableWidget_14.setItem(j+1,3, QtGui.QTableWidgetItem('Total arreas- '))
        self.tableWidget_14.setItem(j+1,4, QtGui.QTableWidgetItem(str(tt)))        

    def daily_collectible(self):
        self.tableWidget_18.setRowCount(0)
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        d1=self.dateEdit_18.date().toPyDate()
        d2=self.dateEdit_26.date().toPyDate()
        delta = d2 - d1
        l=[]

        for i in range(delta.days + 1):
            date=str( d1 + datetime.timedelta(days=i))
            c.execute("select loans.loan_no,customers.name,loans.amount,loans.inst_val,customers.tp,loans.date from loans,customers where loans.date='%s' and customers.nic=loans.nic_no and loans.loan_no like '%s'"%(date,'%BL/D%'))
            data=c.fetchall()
            if data:
                l+=data
        self.tableWidget_18.setRowCount(len(l)+1)
        tt=0
        j=0
        for j,i in enumerate(l):
                    self.tableWidget_18.setItem(j,0, QtGui.QTableWidgetItem(i[0]))
                    self.tableWidget_18.setItem(j,1, QtGui.QTableWidgetItem(i[1]))
                    self.tableWidget_18.setItem(j,2, QtGui.QTableWidgetItem(i[2]))
                    self.tableWidget_18.setItem(j,3, QtGui.QTableWidgetItem(str(i[3])))
                    self.tableWidget_18.setItem(j,4, QtGui.QTableWidgetItem(str(i[5])))
                    tt+=float(i[3])
                    if un=='finance' and tt>200000:
                        break                    
        self.tableWidget_18.setItem(j+1,2, QtGui.QTableWidgetItem(''))
        self.tableWidget_18.setItem(j+1,3, QtGui.QTableWidgetItem(''))
        self.tableWidget_18.setItem(j+1,2, QtGui.QTableWidgetItem('Total Installments- '))
        self.tableWidget_18.setItem(j+1,3, QtGui.QTableWidgetItem(str(tt)))     


    def week_collectible(self):
        self.tableWidget_16.setRowCount(0)
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        d1=self.dateEdit_16.date().toPyDate()
        d2=self.dateEdit_25.date().toPyDate()
        delta = d2 - d1
        l=[]
        for i in range(delta.days + 1):
            date=str( d1 + datetime.timedelta(days=i))
            c.execute("select loans.loan_no,customers.name,loans.amount,loans.inst_val,customers.tp,loans.date from loans,customers where loans.date='%s' and customers.nic=loans.nic_no and loans.loan_no like '%s'"%(date,'%BL/W%'))

            data=c.fetchall()
            if data:
                l+=data
        self.tableWidget_16.setRowCount(len(l)+1)
        tt=0
        j=0
        for j,i in enumerate(l):
                    self.tableWidget_16.setItem(j,0, QtGui.QTableWidgetItem(i[0]))
                    self.tableWidget_16.setItem(j,1, QtGui.QTableWidgetItem(i[1]))
                    self.tableWidget_16.setItem(j,2, QtGui.QTableWidgetItem(i[2]))
                    self.tableWidget_16.setItem(j,3, QtGui.QTableWidgetItem(str(i[3])))
                    self.tableWidget_16.setItem(j,4, QtGui.QTableWidgetItem(str(i[5])))
                    tt+=float(i[3])
                    if un=='finance' and tt>200000:
                        break
        self.tableWidget_16.setItem(j+1,2, QtGui.QTableWidgetItem(''))
        self.tableWidget_16.setItem(j+1,3, QtGui.QTableWidgetItem(''))
        self.tableWidget_16.setItem(j+1,2, QtGui.QTableWidgetItem('Total Installments- '))
        self.tableWidget_16.setItem(j+1,3, QtGui.QTableWidgetItem(str(tt)))     

    def mon_collectible(self):
        self.tableWidget_12.setRowCount(0)
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        d1=self.dateEdit_15.date().toPyDate()
        d2=self.dateEdit_24.date().toPyDate()
        delta = d2 - d1
        l=[]
        for i in range(delta.days + 1):
            date=str( d1 + datetime.timedelta(days=i))
            c.execute("select loans.loan_no,customers.name,loans.amount,loans.inst_val,customers.tp,loans.date from loans,customers where loans.date='%s' and customers.nic=loans.nic_no and loans.loan_no like '%s'"%(date,'%DL%'))
            data=c.fetchall()
    
            if data:
                l+=data
        print un
        self.tableWidget_12.setRowCount(len(l)+1)
        tt=0
        j=0
        for j,i in enumerate(l):
                    self.tableWidget_12.setItem(j,0, QtGui.QTableWidgetItem(i[0]))
                    self.tableWidget_12.setItem(j,1, QtGui.QTableWidgetItem(i[1]))
                    self.tableWidget_12.setItem(j,2, QtGui.QTableWidgetItem(i[2]))
                    self.tableWidget_12.setItem(j,3, QtGui.QTableWidgetItem(str(i[3])))
                    self.tableWidget_12.setItem(j,4, QtGui.QTableWidgetItem(str(i[4])))
                    tt+=float(i[3])
                    if un=='finance' and tt>400000:
                        break
        self.tableWidget_12.setItem(j+1,2, QtGui.QTableWidgetItem('Total Installments- '))
        self.tableWidget_12.setItem(j+1,3, QtGui.QTableWidgetItem(str(tt)))        


    def col_register(self):
        self.tableWidget_11.setRowCount(0)
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        d1=self.dateEdit_37.date().toPyDate()
        d2=self.dateEdit_36.date().toPyDate()
        delta = d2 - d1
        l=[]
        if self.comboBox_21.currentText()== 'Monthly':
            filter1='%DL%'
        elif self.comboBox_21.currentText()== 'Weekly':
            filter1='%BL/W%'
        elif self.comboBox_21.currentText()== 'Daily':
            filter1='%BL/D%'
        for i in range(delta.days + 1):
            date=str( d1 + datetime.timedelta(days=i))
            c.execute("select receipts.date,loans.loan_no,loans.int_inst,loans.part_pay,(select sum(d_c) from receipts where  loans.loan_no=receipts.loan_no ),loans.inv_charge from  loans,receipts where loans.date ='%s' and loans.loan_no like '%s' group by loans.loan_no"%(date,filter1))
            l+=c.fetchall()
        self.tableWidget_11.setRowCount(len(l)+1)
        rsu=0
        for j,i in enumerate(l):
            self.tableWidget_11.setItem(j,0, QtGui.QTableWidgetItem(i[0]))
            self.tableWidget_11.setItem(j,1, QtGui.QTableWidgetItem(i[1]))
            self.tableWidget_11.setItem(j,2, QtGui.QTableWidgetItem(i[2]))
            self.tableWidget_11.setItem(j,3, QtGui.QTableWidgetItem(str(i[3])))
            self.tableWidget_11.setItem(j,4, QtGui.QTableWidgetItem(str(i[4])))
            self.tableWidget_11.setItem(j,5, QtGui.QTableWidgetItem(str(i[5])))
            self.tableWidget_11.setItem(j,6, QtGui.QTableWidgetItem(str(float(i[2])+float(i[3])+float(i[4])+float(i[5]))))
            rsu+=float(i[2])+float(i[3])+float(i[4])+float(i[5])
        self.tableWidget_11.setItem(j+1,5, QtGui.QTableWidgetItem(str('Total D/P')))
        self.tableWidget_11.setItem(j+1,6, QtGui.QTableWidgetItem(str(rsu)))


    def loan_accounts(self):
        self.tableWidget_10.setRowCount(0)
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        d1=self.dateEdit_13.date().toPyDate()
        d2=self.dateEdit_35.date().toPyDate()
        delta = d2 - d1

        l=[]
        if self.comboBox_20.currentText()== 'Monthly':
            filter1='%DL%'
        elif self.comboBox_20.currentText()== 'Weekly':
            filter1='%BL/W%'
        elif self.comboBox_20.currentText()== 'Daily':
            filter1='%BL/D%'
        for i in range(delta.days + 1):
            date=str( d1 + datetime.timedelta(days=i))
            c.execute("select loans.date,loans.loan_no,loans.amount,loans.inst_val,loans.part_pay,receipts.down_pay,receipts.d_c,(select sum(down_pay) from receipts where  loans.loan_no=receipts.loan_no ),receipts.r_no from  loans,receipts where loans.date ='%s' and loans.loan_no like '%s' and loans.loan_no=receipts.loan_no and receipts.down_pay>1"%(date,filter1))
            l+=c.fetchall()
        self.tableWidget_10.setRowCount(len(l))
        for j,i in enumerate(l):
            try:
                p_p=float(i[4])
            except:
                p_p=0
            self.tableWidget_10.setItem(j,0, QtGui.QTableWidgetItem(i[0]))
            self.tableWidget_10.setItem(j,1, QtGui.QTableWidgetItem(i[1]))
            self.tableWidget_10.setItem(j,2, QtGui.QTableWidgetItem(str(float(i[2])+p_p)))
            self.tableWidget_10.setItem(j,3, QtGui.QTableWidgetItem(i[2]))
            self.tableWidget_10.setItem(j,4, QtGui.QTableWidgetItem(str(i[3])))
            self.tableWidget_10.setItem(j,5, QtGui.QTableWidgetItem(str(i[4])))
            self.tableWidget_10.setItem(j,6, QtGui.QTableWidgetItem(str(i[5])))
            self.tableWidget_10.setItem(j,7, QtGui.QTableWidgetItem(str(i[6])))
            self.tableWidget_10.setItem(j,8, QtGui.QTableWidgetItem(str(float(i[7])+float(i[4])+float(i[6]))))
            self.tableWidget_10.setItem(j,9, QtGui.QTableWidgetItem('000'+str(i[8])))

    def loan_register(self):
        self.tableWidget_9.setRowCount(0)
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        d1=self.dateEdit_12.date().toPyDate()
        l=[]
        if self.comboBox_19.currentText()== 'Monthly':
            filter1='%DL%'
        elif self.comboBox_19.currentText()== 'Weekly':
            filter1='%BL/W%'
        elif self.comboBox_19.currentText()== 'Daily':
            filter1='%BL/D%'
        for i in range(30):
            date=str( d1 + datetime.timedelta(days=i))
            c.execute("select loans.date,pay_dates.date,loans.loan_no,customers.name,customers.address,customers.tp,loans.amount from loans,customers,pay_dates where loans.date ='%s' and loans.loan_no like '%s' and loans.nic_no=customers.nic and loans.loan_no=pay_dates.loan_no group by pay_dates.loan_no "%(date,filter1))
            l+=c.fetchall()
        self.tableWidget_9.setRowCount(len(l)+1)
        tt=0
        print un
        for j,i in enumerate(l):
            self.tableWidget_9.setItem(j,0, QtGui.QTableWidgetItem(i[0]))
            self.tableWidget_9.setItem(j,1, QtGui.QTableWidgetItem(i[2]))
            self.tableWidget_9.setItem(j,2, QtGui.QTableWidgetItem(i[3]))
            self.tableWidget_9.setItem(j,3, QtGui.QTableWidgetItem(i[4]))
            self.tableWidget_9.setItem(j,4, QtGui.QTableWidgetItem(str(i[5])))
            self.tableWidget_9.setItem(j,5, QtGui.QTableWidgetItem(str(i[6])))
            self.tableWidget_9.setItem(j,6, QtGui.QTableWidgetItem(str(i[1])))
            tt+=float(i[6])
            if un=='finance' and tt>800000:
                        break
        self.tableWidget_9.setItem(j+1,4, QtGui.QTableWidgetItem('Total Amount - '))
        self.tableWidget_9.setItem(j+1,5, QtGui.QTableWidgetItem(str(tt)))
        
        

    def intrst_collections(self):
        self.tableWidget_7.setRowCount(0)
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        d1=self.dateEdit_7.date().toPyDate()
        d2=self.dateEdit_8.date().toPyDate()
        delta = d2 - d1
        l=[]
        if self.comboBox_11.currentText()== 'Monthly':
            filter1='%DL%'
        elif self.comboBox_11.currentText()== 'Weekly':
            filter1='%BL/W%'
        elif self.comboBox_11.currentText()== 'Daily':
            filter1='%BL/D%'
        for i in range(delta.days + 1):
            date=str( d1 + datetime.timedelta(days=i))
            c.execute("select receipts.loan_no,receipts.date,loans.amount,loans.inst_val,loans.period,loans.interest from receipts,loans where receipts.loan_no=loans.loan_no and receipts.date='%s' and loans.loan_no like '%s'"%(date,filter1))
            data=c.fetchall()
            if data:
                l+=data
        self.tableWidget_7.setRowCount(len(l)+1)
        tt=0
        for j,i in enumerate(l):
                    self.tableWidget_7.setItem(j,0, QtGui.QTableWidgetItem(i[0]))
                    self.tableWidget_7.setItem(j,1, QtGui.QTableWidgetItem(i[2]))
                    self.tableWidget_7.setItem(j,2, QtGui.QTableWidgetItem(str(float(i[5])/float(i[4].split()[0]))))
                    self.tableWidget_7.setItem(j,3, QtGui.QTableWidgetItem(i[3]))
                    self.tableWidget_7.setItem(j,4, QtGui.QTableWidgetItem(str(i[1]))) 
                    tt+=float(i[5])/float(i[4].split()[0])
        self.tableWidget_7.setItem(j+1,1, QtGui.QTableWidgetItem('Total Interest- '))
        self.tableWidget_7.setItem(j+1,2, QtGui.QTableWidgetItem(str(tt)))                 



    def inst_collections(self):
        self.tableWidget_6.setRowCount(0)
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        d1=self.dateEdit_5.date().toPyDate()
        d2=self.dateEdit_6.date().toPyDate()
        delta = d2 - d1
        l=[]
        if self.comboBox_10.currentText()== 'Monthly':
            filter1='%DL%'
        elif self.comboBox_10.currentText()== 'Weekly':
            filter1='%BL/W%'
        elif self.comboBox_10.currentText()== 'Daily':
            filter1='%BL/D%'
        for i in range(delta.days + 1):
            date=str( d1 + datetime.timedelta(days=i))
            c.execute("select receipts.loan_no,receipts.date,loans.amount,loans.inst_val,receipts.balance,receipts.r_no from receipts,loans where receipts.loan_no=loans.loan_no and receipts.date='%s' and loans.loan_no like '%s'"%(date,filter1))
            data=c.fetchall()
            if data:
                l+=data
        self.tableWidget_6.setRowCount(len(l)+1)
        tt=0
        for j,i in enumerate(l):
                    self.tableWidget_6.setItem(j,0, QtGui.QTableWidgetItem(i[0]))
                    self.tableWidget_6.setItem(j,1, QtGui.QTableWidgetItem(i[2]))
                    self.tableWidget_6.setItem(j,2, QtGui.QTableWidgetItem(i[3]))
                    self.tableWidget_6.setItem(j,3, QtGui.QTableWidgetItem(str(i[5])))
                    self.tableWidget_6.setItem(j,4, QtGui.QTableWidgetItem(i[1]))
                    self.tableWidget_6.setItem(j,5, QtGui.QTableWidgetItem(str(i[4])))
                    tt+=float(i[3])
        self.tableWidget_6.setItem(j+1,1, QtGui.QTableWidgetItem('Total Installments- '))
        self.tableWidget_6.setItem(j+1,2, QtGui.QTableWidgetItem(str(tt)))                 


    def intrst_collectible(self):
        self.tableWidget_5.setRowCount(0)
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        d1=self.dateEdit_3.date().toPyDate()
        d2=self.dateEdit_4.date().toPyDate()
        delta = d2 - d1
        l=[]
        if self.comboBox_9.currentText()== 'Monthly':
            filter1='%DL%'
        elif self.comboBox_9.currentText()== 'Weekly':
            filter1='%BL/W%'
        elif self.comboBox_9.currentText()== 'Daily':
            filter1='%BL/D%'
        for i in range(delta.days + 1):
            date=str( d1 + datetime.timedelta(days=i))
            c.execute("select loans.loan_no,loans.date,loans.amount,loans.period,loans.interest,loans.inst_val,balance.balance from loans,balance where loans.date='%s' and loans.loan_no=balance.loan_no and loans.loan_no like '%s'"%(date,filter1))
            data=c.fetchall()
            if data:
                l+=data
        self.tableWidget_5.setRowCount(len(l)+1)
        tt=0
        for j,i in enumerate(l):
                    self.tableWidget_5.setItem(j,0, QtGui.QTableWidgetItem(i[0]))
                    self.tableWidget_5.setItem(j,1, QtGui.QTableWidgetItem(i[2]))
                    self.tableWidget_5.setItem(j,2, QtGui.QTableWidgetItem(str(float(i[4])/float(i[3].split()[0]))))
                    self.tableWidget_5.setItem(j,3, QtGui.QTableWidgetItem(str(i[5])))
                    self.tableWidget_5.setItem(j,4, QtGui.QTableWidgetItem(i[1])) 
                    tt+=float(i[4])/float(i[3].split()[0])
        self.tableWidget_5.setItem(j+1,1, QtGui.QTableWidgetItem('Total Interest- '))
        self.tableWidget_5.setItem(j+1,2, QtGui.QTableWidgetItem(str(tt)))

    def inst_collectible(self):
        self.tableWidget_4.setRowCount(0)
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        d1=self.dateEdit.date().toPyDate()
        d2=self.dateEdit_2.date().toPyDate()
        delta = d2 - d1
        l=[]
        if self.comboBox_8.currentText()== 'Monthly':
            filter1='%DL%'
        elif self.comboBox_8.currentText()== 'Weekly':
            filter1='%BL/W%'
        elif self.comboBox_8.currentText()== 'Daily':
            filter1='%BL/D%'
        for i in range(delta.days + 1):
            date=str( d1 + datetime.timedelta(days=i))

            c.execute("select loans.loan_no,loans.date,loans.amount,loans.inst_val,balance.balance from loans,balance where loans.date='%s' and loans.loan_no=balance.loan_no and loans.loan_no like '%s'"%(date,filter1))
            data=c.fetchall()
            if data:
                l+=data
        self.tableWidget_4.setRowCount(len(l)+1)
        tt=0
        for j,i in enumerate(l):
                    self.tableWidget_4.setItem(j,0, QtGui.QTableWidgetItem(i[0]))
                    self.tableWidget_4.setItem(j,1, QtGui.QTableWidgetItem(i[2]))
                    self.tableWidget_4.setItem(j,2, QtGui.QTableWidgetItem(i[3]))
                    self.tableWidget_4.setItem(j,3, QtGui.QTableWidgetItem(str(i[1])))
                    self.tableWidget_4.setItem(j,4, QtGui.QTableWidgetItem(str(i[4])))
                    tt+=float(i[3])
        self.tableWidget_4.setItem(j+1,1, QtGui.QTableWidgetItem('Total Installments- '))
        self.tableWidget_4.setItem(j+1,2, QtGui.QTableWidgetItem(str(tt)))
                
    def day_all_receipts(self):
        self.tableWidget_3.setRowCount(0)
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        c.execute("select receipts.r_no,receipts.tr_no,receipts.loan_no,time,receipts.cashier,loans.amount,receipts.total from receipts,loans where receipts.loan_no=loans.loan_no and receipts.date='%s'"%(datetime.datetime.now().strftime('%Y-%m-%d')))
        details=c.fetchall()
        self.tableWidget_3.setRowCount(len(details)+1)
        tt=0
        for j,i in enumerate(details):
                    self.tableWidget_3.setItem(j,0, QtGui.QTableWidgetItem('000'+str(i[0])))
                    self.tableWidget_3.setItem(j,1, QtGui.QTableWidgetItem(i[1]))
                    self.tableWidget_3.setItem(j,2, QtGui.QTableWidgetItem(i[2]))
                    self.tableWidget_3.setItem(j,3, QtGui.QTableWidgetItem(str(i[6])))
                    self.tableWidget_3.setItem(j,4, QtGui.QTableWidgetItem(str(i[3])))
                    self.tableWidget_3.setItem(j,5, QtGui.QTableWidgetItem(str(i[4])))
                    tt+=float(i[6])
        self.tableWidget_3.setItem(j+1,2, QtGui.QTableWidgetItem('Total Amount- '))
        self.tableWidget_3.setItem(j+1,3, QtGui.QTableWidgetItem(str(tt)))

    def deb_card_fill(self):
        self.tableWidget_2.setRowCount(0)
        self.label_37.setText('')
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        if self.lineEdit_43.text()!='':
            loan_no=self.lineEdit_43.text()
            c.execute("select nic_no,period,purpose,amount,part_pay,interest,tt,t_amount,int_inst,inst_val,int_rate,inst_no from loans where loan_no='%s'"%(loan_no))
            try:
                alld=c.fetchall()[0]
                nic=alld[0]
                c.execute("select name,address,tp from customers where nic='%s'"%(nic))
                nm=c.fetchall()
                self.lineEdit_40.setText(nm[0][2])
                self.plainTextEdit_11.clear()
                self.plainTextEdit_14.clear()
                self.plainTextEdit_11.insertPlainText(nm[0][1])
                self.plainTextEdit_14.insertPlainText(nm[0][0])
                self.lineEdit_36.setText(alld[11]+' '+alld[1].split()[-1])
                self.lineEdit_42.setText(alld[2])
                self.lineEdit_41.setText(alld[3])
                self.lineEdit_44.setText(alld[4])
                self.lineEdit_45.setText(alld[5])
                self.lineEdit_49.setText(alld[6])
                self.lineEdit_48.setText(alld[7])
                self.lineEdit_47.setText(alld[8])
                self.lineEdit_46.setText(alld[9])
                c.execute("select total-balance from balance where loan_no='%s'"%(loan_no))
                bal=float(c.fetchone()[0])
                self.lineEdit_50.setText(str(float(bal)))
                c.execute("select date,r_no,arreas,balance from receipts where loan_no='%s'"%(loan_no))
                details=c.fetchall()
                self.tableWidget_2.setRowCount(len(details))
                for j,i in enumerate(details):
                    self.tableWidget_2.setItem(j,0, QtGui.QTableWidgetItem(i[0]))
                    self.tableWidget_2.setItem(j,1, QtGui.QTableWidgetItem('000'+str(i[1])))
                    self.tableWidget_2.setItem(j,2, QtGui.QTableWidgetItem(str(int(i[2])+int(alld[9]))))
                    self.tableWidget_2.setItem(j,3, QtGui.QTableWidgetItem(alld[10]))
                    self.tableWidget_2.setItem(j,4, QtGui.QTableWidgetItem(i[3]))
            except:
                self.label_37.setText('Contract number not valid!')
            
            
            
        else:
            self.label_37.setText('Please Enter Contract No')


    def deb_card_loan_no_set(self):
        if str(self.comboBox_18.currentText())=='Monthly':
            self.lineEdit_43.setText('MT/DL/')
        elif str(self.comboBox_18.currentText())=='Weekly':
            self.lineEdit_43.setText('MT/BL/W/')
        elif str(self.comboBox_18.currentText())=='Daily':
            self.lineEdit_43.setText('MT/BL/D/')

    def add_and_print_receipt(self):
        self.print_receipt()
        self.add_receipt()
            
    def add_receipt(self):
        try:
            float(self.lineEdit_57.text())
        except:
            self.lineEdit_57.setText('0')
        self.label_35.setText('Please wait!!')
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        self.label_35.setText('')
        self.label_36.setText('')
        loan_no=self.lineEdit_64.text()
        c.execute("select total-balance from balance where loan_no='%s'"%(loan_no))
        balance=c.fetchone()[0]
        if float(self.lineEdit_75.text())+float(self.lineEdit_54.text())+float(self.lineEdit_55.text())+float(self.lineEdit_57.text())>float(balance):
            self.label_35.setText('Payment larger than loan balance!')
        else:
            if self.lineEdit_64.text()!='' and self.lineEdit_60.text()!='' :
                try:
                    sd=str(float(self.lineEdit_57.text()))
                except:
                    sd='0.0'
                if self.lineEdit_75.text()!='' and self.lineEdit_75.text()!='0':
                  try:
                    c.execute("insert into part_pay(loan_no,part_pay) values ('%s','%s')"%(loan_no,self.lineEdit_75.text()))
                    conn.commit()
                    c.execute("update balance set balance=balance+%s+%s+%s where loan_no='%s'"%(sd,self.lineEdit_54.text(),self.lineEdit_55.text(),self.lineEdit_64.text()))
                    conn.commit()
                    c.execute("select balance from balance where loan_no='%s'"%(self.lineEdit_64.text()))
                    bal=float(c.fetchone()[0])
                    c.execute("select t_amount from loans where loan_no='%s'"%(self.lineEdit_64.text()))
                    t_amount=c.fetchone()[0]       
                    c.execute("insert into receipts(installment,r_no,tr_no,loan_no,cashier,arreas,def_charge,down_pay,inv_charge,d_c,stamp,total,date,balance,time) values(%s,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(self.lineEdit_54.text(),self.lineEdit_63.text(),self.lineEdit_62.text(),self.lineEdit_64.text(),self.lineEdit_65.text(),self.lineEdit_55.text(),self.lineEdit_56.text(),sd,self.lineEdit_58.text(),self.lineEdit_59.text(),self.lineEdit_61.text(),self.lineEdit_60.text(),self.dateEdit_19.date().toPyDate(),str(float(self.lineEdit_81.text())-(float(self.lineEdit_55.text())+float(self.lineEdit_54.text())+float(self.lineEdit_57.text()))),datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S')))
                    conn.commit()
                    self.label_35.setText('Receipt Added Succssfully!')
                    self.record_activity('New Receipt Added %s'%(str(self.lineEdit_63.text())))
                    self.lineEdit_54.setText('')
                    self.lineEdit_55.setText('')
                    self.lineEdit_56.setText('')
                    self.lineEdit_57.setText('')
                    self.lineEdit_58.setText('')
                    self.lineEdit_59.setText('')
                    self.lineEdit_60.setText('')
                    self.lineEdit_61.setText('')
                    self.lineEdit_62.setText('')
                    self.lineEdit_63.setText('')
                    self.lineEdit_64.setText('')
                    self.lineEdit_65.setText('')
                    self.lineEdit_80.setText('')
                    self.lineEdit_81.setText('')
                    self.lineEdit_75.setText('')
                    self.plainTextEdit_12.clear()
                    self.plainTextEdit_13.clear()
                    self.listWidget.clear() 
                    self.receipt_loan_no_set()

                  except:
                    self.label_35.setText('Part Payment already added for this loan')
                else:
                    c.execute("update balance set balance=balance+%s+%s+%s where loan_no='%s'"%(sd,self.lineEdit_54.text(),self.lineEdit_55.text(),self.lineEdit_64.text()))
                    conn.commit()
                    c.execute("select balance from balance where loan_no='%s'"%(self.lineEdit_64.text()))
                    bal=float(c.fetchone()[0])
                    c.execute("select t_amount from loans where loan_no='%s'"%(self.lineEdit_64.text()))
                    t_amount=c.fetchone()[0]       
                    c.execute("insert into receipts(installment,r_no,tr_no,loan_no,cashier,arreas,def_charge,down_pay,inv_charge,d_c,stamp,total,date,balance,time) values(%s,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(self.lineEdit_54.text(),self.lineEdit_63.text(),self.lineEdit_62.text(),self.lineEdit_64.text(),self.lineEdit_65.text(),self.lineEdit_55.text(),self.lineEdit_56.text(),sd,self.lineEdit_58.text(),self.lineEdit_59.text(),self.lineEdit_61.text(),self.lineEdit_60.text(),self.dateEdit_19.date().toPyDate(),str(float(self.lineEdit_81.text())-(float(self.lineEdit_55.text())+float(self.lineEdit_54.text())+float(self.lineEdit_57.text()))),datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S')))
                    conn.commit()
                    self.label_35.setText('Receipt Added Succssfully!')
                    self.record_activity('New Receipt Added %s'%(str(self.lineEdit_63.text())))
                    self.lineEdit_54.setText('')
                    self.lineEdit_55.setText('')
                    self.lineEdit_56.setText('')
                    self.lineEdit_57.setText('')
                    self.lineEdit_58.setText('')
                    self.lineEdit_59.setText('')
                    self.lineEdit_60.setText('')
                    self.lineEdit_61.setText('')
                    self.lineEdit_62.setText('')
                    self.lineEdit_63.setText('')
                    self.lineEdit_64.setText('')
                    self.lineEdit_65.setText('')
                    self.lineEdit_80.setText('')
                    self.lineEdit_81.setText('')
                    self.lineEdit_75.setText('')
                    self.plainTextEdit_12.clear()
                    self.plainTextEdit_13.clear()
                    self.listWidget.clear() 
                    self.receipt_loan_no_set()
                    
            else:
                self.label_35.setText('Please Fill loan number and Total payment!')
    def set_receipt(self):
        self.label_36.setText('')
        self.lineEdit_57.setEnabled(True)
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        loan_no=str(self.lineEdit_64.text())
        c.execute("select loan_no from cancelled")
        if loan_no in c.fetchall()[0]:
            self.label_36.setText('Loan already cancelled!')
        else:
            try:
                c.execute("select total-balance from balance where loan_no='%s'"%(loan_no))
                balance=c.fetchone()[0]
                if balance >0:
                    #self.plainTextEdit_12.clearsf()
                    c.execute("select nic_no,inst_val from loans where loan_no='%s'"%(loan_no))
                    alld=c.fetchall()[0]
                    nic=alld[0]
                    c.execute("select name,address from customers where nic='%s'"%(nic))
                    self.plainTextEdit_12.clear()
                    self.plainTextEdit_13.clear()
                    d=c.fetchall()[0]
                    self.plainTextEdit_12.insertPlainText(d[0])
                    self.plainTextEdit_13.insertPlainText(d[1])
                    print balance,alld
                    if balance<float(alld[1]):
                        inss=balance
                        self.lineEdit_57.setText(str('Balance too low to add down Payment!'))
                        self.lineEdit_57.setEnabled(False)
                    else:
                        inss=alld[1]
                    self.lineEdit_54.setText(str(inss))
                    c.execute("select date from pay_dates where loan_no ='%s'"%(loan_no))
                    a=c.fetchall()
                    d=False
                    x= sorted(map(lambda x:datetime.datetime.strptime(x[0],"%y/%m/%d"),a))
                    try:
                        for i in range(len(x)):
                            if x[i]>datetime.datetime.now():
                                ind=i-1 if i!=0 else 'x'
                                date=x[ind]
                                break
                        d=datetime.datetime.strftime(date,"%y/%m/%d")
                            
                        
                    except Exception as e:
                        print e

                    if not d:
                        arreas='0'
                        def_charge='0'
                    else:
                        c.execute("select installment from pay_dates where loan_no ='%s' and date='%s'"%(loan_no,d))
                        pay=int(c.fetchone()[0])
                        c.execute("select balance from balance where loan_no='%s'"%(loan_no))
                        bal=int(c.fetchone()[0])
                        if bal>=pay:
                            arreas='0'
                            def_charge='0'
                        else:
                            arreas=str(pay-bal)
                            def_inst=float(arreas)/float(alld[1])
                            def_charge=0
                            temp=def_inst*1
                            for i in range(int(def_inst)):
                                    def_charge+=float(3)/(100)*(float(alld[1])*temp)
                                    temp-=1
                    self.lineEdit_55.setText(arreas)
                    self.lineEdit_56.setText(str(def_charge))
                    self.lineEdit_65.setText(un)
                    try:
                        c.execute("select max(r_no) from receipts")
                        self.lineEdit_63.setText('000'+str(int(c.fetchone()[0])+1))
                    except:
                        self.lineEdit_63.setText('0001')
                    c.execute("select date from receipts where loan_no='%s'"%(loan_no))
                    try:
                            last_pay=c.fetchall()[-1][0]
                    except:
                            c.execute("select date from loans where loan_no='%s'"%(loan_no))
                            last_pay=c.fetchall()[0][0]
                            self.lineEdit_80.setText(last_pay)
                    try:
                            self.listWidget.clear()
                            c.execute("select date from pay_dates where loan_no='%s'"%(loan_no))
                            for i in c.fetchall():
                                item = QListWidgetItem(i[0])
                                self.listWidget.addItem(item)
                    except Exception as e:
                            print e
                    c.execute("select total-balance from balance where loan_no='%s'"%(loan_no))
                    balance=c.fetchone()[0]
                    self.lineEdit_81.setText(str(balance))
                else:
                    self.label_36.setText('Loan has been paid completely')
            except Exception as e:
                print e
                self.label_36.setText('Invalid Loan Number!')
    def receipt_total(self):
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        self.label_96.setText('')
        loan_no=self.lineEdit_64.text()
        c.execute("select total-balance from balance where loan_no='%s'"%(loan_no))
        balance=c.fetchone()[0]
        try:
            float(self.lineEdit_57.text())
            if float(self.lineEdit_54.text())+float(self.lineEdit_55.text())+float(self.lineEdit_57.text())+float(self.lineEdit_75.text())>float(balance):
                self.label_96.setText('Payment larger than loan balance!')
            else:
                total=0
                for i in [self.lineEdit_75.text(),self.lineEdit_54.text(),self.lineEdit_55.text(),self.lineEdit_56.text(),self.lineEdit_57.text(),self.lineEdit_58.text(),self.lineEdit_59.text(),self.lineEdit_61.text()]:
                        total+=float(i)
                self.lineEdit_60.setText(str(total))
        except:
            if float(self.lineEdit_54.text())+float(self.lineEdit_55.text())+float(self.lineEdit_75.text())>float(balance):
                self.label_96.setText('Payment larger than loan balance!')
            else:
                total=0
                for i in [self.lineEdit_75.text(),self.lineEdit_54.text(),self.lineEdit_55.text(),self.lineEdit_56.text(),self.lineEdit_58.text(),self.lineEdit_59.text(),self.lineEdit_61.text()]:
                        total+=float(i)
                self.lineEdit_60.setText(str(total))

    def receipt_loan_no_set(self):
        if str(self.comboBox_17.currentText())=='Monthly':
            self.lineEdit_64.setText('MT/DL/')
        elif str(self.comboBox_17.currentText())=='Weekly':
            self.lineEdit_64.setText('MT/BL/W/')
        elif str(self.comboBox_17.currentText())=='Daily':
            self.lineEdit_64.setText('MT/BL/D/')        
 
    def add_paydate(self,period,length,installment,loan_no):
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        if self.lineEdit_26.text()!='':
            now = datetime.datetime.now()
            inst=0
            for i in range(1,int(length)+1):
                    inst+=float(installment)
                    dt=QDate(now.year,now.month,int(self.lineEdit_26.text())).addMonths(i).toPyDate().strftime("%y/%m/%d")
                    c.execute("insert into pay_dates(loan_no,installment,date) values ('%s','%s','%s')"%(loan_no,str(inst),dt))
                    conn.commit()
                
        else:
            if period=='Monthly':
                dt=datetime.date.today().strftime("%y/%m/%d")
                inst=0
                for i in range(int(length)):
                    inst+=float(installment)
                    dt=datetime.datetime.strptime(dt, "%y/%m/%d")
                    dt=(dt+ datetime.timedelta(days=30)).strftime("%y/%m/%d")
                    c.execute("insert into pay_dates(loan_no,installment,date) values ('%s','%s','%s')"%(loan_no,str(inst),dt))
                    conn.commit()
            elif period=='Weekly':
                dt=datetime.date.today().strftime("%y/%m/%d")
                inst=0
                for i in range(int(length)):
                    inst+=float(installment)
                    dt=datetime.datetime.strptime(dt, "%y/%m/%d")
                    dt=(dt+ datetime.timedelta(days=7)).strftime("%y/%m/%d")
                    c.execute("insert into pay_dates(loan_no,installment,date) values ('%s','%s','%s')"%(loan_no,str(inst),dt))
                    conn.commit()
            elif period=='Daily':
                dt=datetime.date.today().strftime("%y/%m/%d")
                inst=0
                for i in range(int(length)):
                    inst+=float(installment)
                    dt=datetime.datetime.strptime(dt, "%y/%m/%d")
                    dt=(dt+ datetime.timedelta(days=1)).strftime("%y/%m/%d")
                    c.execute("insert into pay_dates(loan_no,installment,date) values ('%s','%s','%s')"%(loan_no,str(inst),dt))
                    conn.commit()
    def add_loan(self):
        if 1:
                self.label_34.setText('')
                if self.lineEdit.text()!='' and self.plainTextEdit_2.toPlainText()!='' and self.lineEdit_4.text()!='' and self.lineEdit_9.text()!='' and self.lineEdit_8.text()!='' and self.lineEdit_7.text()!='' and self.lineEdit_6.text()!='' and self.lineEdit_13.text()!='' and self.lineEdit_2.text()!='' and self.lineEdit_15.text()!='' and self.lineEdit_19.text()!='':
                  try:
                    conn = sqlite3.connect('main.db')
                    c=conn.cursor()
                    c.execute("insert into loans (loan_no,nic_no,period,purpose,amount,interest,int_rate,tt,t_amount,inst_no,inst_val,x_bal,int_inst,part_pay,inv_charge,stamps,total,type,date) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(self.lineEdit_2.text(),self.lineEdit.text(),self.comboBox_6.currentText(),self.plainTextEdit.toPlainText(),self.lineEdit_4.text(),self.lineEdit_19.text(),self.comboBox_5.currentText(),self.lineEdit_5.text(),self.lineEdit_9.text(),self.lineEdit_8.text(),self.lineEdit_7.text(),self.lineEdit_6.text(),self.lineEdit_13.text(),self.lineEdit_12.text(),self.lineEdit_11.text(),self.lineEdit_10.text(),self.lineEdit_15.text(),self.comboBox_4.currentText(),datetime.datetime.now().strftime('%Y-%m-%d')))
                    conn.commit()
                    c.execute("update loan_num set type=type+1 where value='%s'"%(str(self.comboBox_4.currentText()).lower()))
                    conn.commit()
                    c.execute("insert into balance (loan_no,installment,balance,total) values ('%s','%s',%s,'%s')"%(self.lineEdit_2.text(),self.lineEdit_7.text(),'0',self.lineEdit_6.text()))
                    conn.commit()
                    self.add_paydate(str(self.comboBox_4.currentText()),self.lineEdit_8.text(),self.lineEdit_7.text(),self.lineEdit_2.text())
                    self.record_activity('New Loan added "%s"'%(self.lineEdit_2.text()))
                    self.label_34.setText('Loan Details Added Successfully!')
                    self.lineEdit.setText('')
                    self.lineEdit_2.setText('')
                    self.lineEdit_4.setText('')
                    self.lineEdit_5.setText('')
                    self.lineEdit_6.setText('')
                    self.lineEdit_7.setText('')
                    self.lineEdit_8.setText('')
                    self.lineEdit_9.setText('')
                    self.lineEdit_19.setText('')
                    self.lineEdit_10.setText('')
                    self.lineEdit_11.setText('')
                    self.lineEdit_12.setText('')
                    self.lineEdit_13.setText('')
                    self.lineEdit_15.setText('')
                    self.lineEdit_26.setText('')
                    self.plainTextEdit.clear()
                    self.plainTextEdit_2.clear()
                  except Exception as E:
                    print E
                    self.label_34.setText('Loan Already exsist!')
                else:
                    self.label_34.setText('Please Fill all the fields!')
                    
        else:
            self.label_34.setText('Invalid Paydate!')
    def total(self):
        self.label_34.setText('')
        if self.lineEdit_10.text()!='' and self.lineEdit_11.text()!='' and self.lineEdit_13.text()!='' and self.lineEdit_12.text()!='':
            try:
                self.lineEdit_15.setText(str(float(self.lineEdit_12.text())+float(self.lineEdit_10.text())+float(self.lineEdit_11.text())+float(self.lineEdit_13.text())))
            except:
                self.label_34.setText('Please Input Correct Values!')
    def set_installment_again(self):
        self.label_34.setText('')
        self.loan_num()
        try:
            t=float(self.lineEdit_9.text())
            inst_no=float(self.lineEdit_8.text())
            inst_val=float(self.lineEdit_7.text())
            self.lineEdit_6.setText(str(inst_no*inst_val))
            self.lineEdit_13.setText(str(t-(inst_no*inst_val)))
            self.total()
        except:
            self.label_34.setText('Please Input Correct Values!')
    def set_installment(self):
        self.label_34.setText('')
        self.loan_num()
        try:
            t=float(self.lineEdit_9.text())
            inst_no=float(self.lineEdit_8.text())
            
            self.lineEdit_7.setText(str(t/inst_no))
            self.lineEdit_6.setText(str(t))
            self.lineEdit_13.setText(str(0))
            self.total()
        except Exception as e:
            print e
            self.label_34.setText('Please Input Correct Values!')
        
    def cal_interest(self):
        self.label_34.setText('')
        self.loan_num()
        self.total()
        try:
            
            amount=float(self.lineEdit_4.text())
            intrest=(int(self.comboBox_5.currentText()[:-1])*amount)/100
            self.lineEdit_19.setText(str(intrest))
            self.lineEdit_9.setText(str(intrest+amount))
            

        except Exception as e:
            if self.lineEdit_4.text()!='' and self.lineEdit_7.text()!='':
                self.label_34.setText('Please Enter Correct Loan Amount')
        t=float(str(intrest+amount))
        inst_no=float(self.lineEdit_8.text())    
        self.lineEdit_7.setText(str(t/inst_no))
        inst_val=float(str(t/inst_no))
        self.lineEdit_6.setText(str(inst_no*inst_val))
        self.lineEdit_13.setText('0')
        
        
    def loan_num(self):
        try:
            conn = sqlite3.connect('main.db')
            c=conn.cursor()
            c.execute("select type from loan_num where value='%s'"%(str(self.comboBox_4.currentText()).lower()))
            res=str(c.fetchone()[0])
            self.lineEdit_2.setText(('MT/DL/' if self.comboBox_4.currentText()=='Monthly' else 'MT/BL/D/' if self.comboBox_4.currentText()=='Daily' else 'MT/BL/W/')+str(self.comboBox_6.currentText()).split()[0]+'/'+res)
        except:
            pass
        #c.execute("select type from loan_num where value='%s'"%(typ))
    def rate_(self):
        if self.comboBox_6.currentText()== '3 Months':
            self.comboBox_5.clear()
            self.comboBox_5.addItem('6%')
        elif self.comboBox_6.currentText()== '6 Months':
            self.comboBox_5.clear()
            self.comboBox_5.addItem('12%')
        elif self.comboBox_6.currentText()== '12 Months':
            self.comboBox_5.clear()
            self.comboBox_5.addItem('24%')
            self.comboBox_5.addItem('22%')
        elif self.comboBox_6.currentText()== '18 Months':
            self.comboBox_5.clear()
            self.comboBox_5.addItem('36%')
        elif self.comboBox_6.currentText()== '24 Months':
            self.comboBox_5.clear()
            self.comboBox_5.addItem('48%')
            self.comboBox_5.addItem('44%')
        elif self.comboBox_6.currentText()== '48 Weeks':
            print 48
            self.comboBox_5.clear()
            self.comboBox_5.addItem('24%')
        elif self.comboBox_6.currentText()== '24 Weeks':
            print 24
            self.comboBox_5.clear()
            self.comboBox_5.addItem('12%')

        elif self.comboBox_6.currentText()== '25 Days':
            self.comboBox_5.clear()
            self.comboBox_5.addItem('5%')
        elif self.comboBox_6.currentText()== '50 Days':
            self.comboBox_5.clear()
            self.comboBox_5.addItem('10%')
        try:
            self.lineEdit_8.setText(str(self.comboBox_6.currentText()).split()[0])
            
        except:
            pass
    def period(self):
        if self.comboBox_4.currentText()== 'Monthly':
            self.lineEdit_26.text()!=''
            self.lineEdit_26.setEnabled(True)
            self.comboBox_5.clear()
            self.comboBox_6.clear()
            self.comboBox_5.addItem('6%')
            self.comboBox_5.addItem('12%')
            self.comboBox_5.addItem('24%')
            self.comboBox_5.addItem('36%')
            self.comboBox_5.addItem('48%')
            self.comboBox_6.addItem('3 Months')
            self.comboBox_6.addItem('6 Months')
            self.comboBox_6.addItem('12 Months')
            self.comboBox_6.addItem('18 Months')
            self.comboBox_6.addItem('24 Months')
        elif self.comboBox_4.currentText()== 'Weekly':
            self.lineEdit_26.text()!=''
            self.lineEdit_26.setEnabled(False)
            self.comboBox_5.clear()
            self.comboBox_6.clear()
            self.comboBox_5.addItem('12%')
            self.comboBox_5.addItem('24%')
            self.comboBox_6.addItem('24 Weeks')
            self.comboBox_6.addItem('48 Weeks')
        elif self.comboBox_4.currentText()== 'Daily':
            self.lineEdit_26.text()!=''
            self.lineEdit_26.setEnabled(False)
            self.comboBox_5.clear()
            self.comboBox_6.clear()
            self.comboBox_5.addItem('5%')
            self.comboBox_5.addItem('10%')
            self.comboBox_6.addItem('25 Days')
            self.comboBox_6.addItem('50 Days')
        self.loan_num()
        
             


    def work_sheet_check(self):
        self.label_33.setText('')
        if self.lineEdit.text()!='':
            try:
                conn = sqlite3.connect('main.db')
                c=conn.cursor()
                c.execute("select name from customers where `nic`='%s'"%(self.lineEdit.text()))
                self.plainTextEdit_2.clear()
                self.plainTextEdit_2.insertPlainText(c.fetchone()[0])
                
                
            except Exception as e:
                self.label_33.setText('No customer exsist with entered NIC no!')
                print e
            self.loan_num()

    def Guaranter_loan_no_set(self):
        if str(self.comboBox_22.currentText())=='Monthly':
            self.lineEdit_100.setText('MT/DL/')
        elif str(self.comboBox_22.currentText())=='Weekly':
            self.lineEdit_100.setText('MT/BL/W/')
        elif str(self.comboBox_22.currentText())=='Daily':
            self.lineEdit_100.setText('MT/BL/D/')
            
    def add_guaranter(self):
        self.label_190.setText('')
        if self.plainTextEdit_9.toPlainText()!='' and self.plainTextEdit_16.toPlainText()!='' and self.lineEdit_100.text()!='' and self.lineEdit_94.text()!='' and self.lineEdit_95.text()!='' and self.lineEdit_96.text()!='' and self.lineEdit_97.text()!='':
            conn = sqlite3.connect('main.db')
            c=conn.cursor()
            try:
                c.execute("select loan_no from loans")
                loans=map( lambda x:x[0],c.fetchall())
                if self.lineEdit_100.text() in loans:
                    c.execute("insert into guaranter(loan_no,name,nic,tp,address,age,occupation,office_address,office_pn,spouse) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(self.lineEdit_100.text(),self.plainTextEdit_9.toPlainText(),self.lineEdit_96.text(),self.lineEdit_95.text(),self.plainTextEdit_16.toPlainText(),self.lineEdit_94.text(),self.lineEdit_97.text(),self.plainTextEdit_19.toPlainText(),self.lineEdit_99.text(),self.plainTextEdit_20.toPlainText()))
                    conn.commit()
                    self.lineEdit_94.setText('')
                    self.lineEdit_95.setText('')
                    self.lineEdit_96.setText('')
                    self.lineEdit_97.setText('')
                    self.plainTextEdit_9.clear()
                    self.plainTextEdit_16.clear()
                    self.lineEdit_100.setText('')
                    self.lineEdit_99.setText('')
                    self.plainTextEdit_19.clear()
                    self.plainTextEdit_20.clear()
                    self.label_190.setText('Guaranter Added Successfully')
                    self.Guaranter_loan_no_set()
                else:
                    self.label_190.setText('Invalid Loan No')
            except:
                self.label_190.setText('Please Enter Valid Details')
        else:
            self.label_190.setText('Please Enter all the Details')
            
    def getfile(self):
      fname = QFileDialog.getOpenFileName(self, 'Open Customer Image', 
         'c:\\',"Image files (*.jpg *.png)")
      self.label_189.setText(fname)    

    def add_customer(self):
        self.label_30.setText('')
        if self.plainTextEdit_4.toPlainText()!='' and self.plainTextEdit_5.toPlainText()!='' and self.lineEdit_3.text()!='' and self.lineEdit_14.text()!='' and self.lineEdit_17.text()!='' and self.lineEdit_18.text()!='':
            conn = sqlite3.connect('main.db')
            c=conn.cursor()
            try:
                cm=str(self.label_189.text())
                print cm
                if len(cm)<4:
                    cm='noimagefound.jpg'
                print cm
                c.execute("insert into customers(nic,name,address,age,occupation,tp) values ('%s','%s','%s','%s','%s','%s')"%(self.lineEdit_3.text(),self.comboBox_3.currentText()+self.plainTextEdit_4.toPlainText(),self.plainTextEdit_5.toPlainText(),self.lineEdit_17.text(),self.lineEdit_18.text(),self.lineEdit_14.text()))
                conn.commit()
                c.execute("insert into cus_other(nic,office_address,office_pn,spouse,image) values ('%s','%s','%s','%s','%s')"%(self.lineEdit_3.text(),self.plainTextEdit_17.toPlainText(),self.lineEdit_98.text(),self.comboBox_15.currentText()+self.plainTextEdit_18.toPlainText(),cm))
                conn.commit()
                self.label_30.setText('Customer details added successfully!')
                self.record_activity('Added new customer "%s"'%(self.lineEdit_3.text()))
                self.lineEdit_3.setText('')
                self.lineEdit_14.setText('')
                self.lineEdit_17.setText('')
                self.lineEdit_18.setText('')
                self.plainTextEdit_4.clear()
                self.plainTextEdit_5.clear()
                self.lineEdit_98.setText('')
                self.plainTextEdit_17.clear()
                self.plainTextEdit_18.clear()
                self.label_189.setText('') 
            except Exception as e:
                print e
                self.label_30.setText('Customer already exsist!')
        else:
            self.label_30.setText('Please fill all Details!')

    def delete_user(self):
        self.label_27.setText('')

        if hashlib.md5(str(self.lineEdit_76.text())).hexdigest()==pw[0]:
            conn = sqlite3.connect('main.db')
            c=conn.cursor()
            c.execute("delete from users where username='%s'"%(self.comboBox_2.currentText()))
            conn.commit()
            self.record_activity('Deleted User "%s"'%(self.comboBox_2.currentText()))
            self.label_27.setText('User Deleted Successfully!')
            self.change_layout()
            self.lineEdit_76.setText('')
        else:
            self.label_27.setText('Incorrect Password!')
    def add_user(self):
        self.label_28.setText('')
        if self.lineEdit_66.text()!='' and self.lineEdit_71.text()!='' and self.lineEdit_72.text()!='' and self.lineEdit_73.text()!='' and self.lineEdit_74.text()!='':
            conn = sqlite3.connect('main.db')
            c=conn.cursor()
            priv='yes' if self.checkBox.isChecked() else 'no'
            c.execute("insert into users(username,password,name,telephone,address,privileges) values ('%s','%s','%s','%s','%s','%s')"%(self.lineEdit_73.text(),hashlib.md5(str(self.lineEdit_74.text())).hexdigest(),self.lineEdit_66.text(),self.lineEdit_72.text(),self.lineEdit_71.text(),priv))
            conn.commit()
            self.record_activity('Created New User "%s"'%(self.lineEdit_73.text()))
            self.label_28.setText('User Added Successfully!')
            self.change_layout()
        else:
            self.label_28.setText('Please Check all fields!')
    def change_layout(self):
        self.comboBox.clear()
        self.comboBox_2.clear() 
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        c.execute("select privileges from users where `username`='%s'"%(un))
        if c.fetchone()[0]=='yes':
            self.groupBox_7.setEnabled(True)
            self.groupBox_8.setEnabled(True)
            self.groupBox_9.setEnabled(True)
            c.execute("select username from users where `username`!='%s'"%(un))
            for i in c.fetchall():
                self.comboBox.addItem(i[0])
                self.comboBox_2.addItem(i[0])

    def view_other_user(self):
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        c.execute("select name,address,telephone from users where `username`='%s'"%(self.comboBox.currentText()))
        details=c.fetchall()
        self.lineEdit_53.setText(details[0][0])
        self.lineEdit_69.setText(details[0][1])
        self.lineEdit_70.setText(str(details[0][2]))
        c.execute("select state,date,time from logins where `username`='%s'"%(self.comboBox.currentText()))
        details=list(c.fetchall())[::-1]
        self.tableWidget_15.setRowCount(len(details))
        for j,i in enumerate(details):
            self.tableWidget_15.setItem(j,0, QtGui.QTableWidgetItem(i[0]))
            self.tableWidget_15.setItem(j,1, QtGui.QTableWidgetItem(i[1]))
            self.tableWidget_15.setItem(j,2, QtGui.QTableWidgetItem(str(i[2])))
        
    def record_activity(self,activity):
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        c.execute("insert into logins(username,date,time,state) values('%s','%s','%s','%s')"%(un,str(datetime.datetime.now()).split()[0],str(datetime.datetime.now()).split()[1],activity))
        conn.commit()
    
    def change_password(self):
        self.label_29.setText('')
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        c.execute("select password from users where `username`='%s'"%(un))
        r_pw=c.fetchone()[0]
        if hashlib.md5(str(self.lineEdit_77.text())).hexdigest()==r_pw and str(self.lineEdit_78.text())!='' and str(self.lineEdit_78.text())!=' ':
            c.execute("update users set password='%s'where username='%s'"%(hashlib.md5(str(self.lineEdit_78.text())).hexdigest(),un))
            conn.commit()
            self.record_activity('Login Password Changed')
            self.label_29.setText('Password Changed Successfully!')
        else:
            self.label_29.setText('Please Enter Correct Password!')
        
        
    def current_user(self):
        global un
        self.change_layout()
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        c.execute("select * from users where `username`='%s'"%(un))
        details=list(c.fetchall())
        self.lineEdit_37.setText(details[0][2])
        self.lineEdit_52.setText(details[0][0])
        self.lineEdit_68.setText(details[0][4])
        self.lineEdit_67.setText(str(details[0][3]))
        c.execute("select * from logins where `username`='%s'"%(un))
        details=list(c.fetchall())[::-1]
        self.tableWidget_13.setRowCount(len(details))
        for j,i in enumerate(details):
            self.tableWidget_13.setItem(j,0, QtGui.QTableWidgetItem(i[0]))
            self.tableWidget_13.setItem(j,1, QtGui.QTableWidgetItem(i[3]))
            self.tableWidget_13.setItem(j,2, QtGui.QTableWidgetItem(i[1]))
            self.tableWidget_13.setItem(j,3, QtGui.QTableWidgetItem(i[2]))
    def logout(self):
        try:
            self.label_38.setText('')
            self.Automatic_backup()
        except Exception as e:
            print e
            self.label_38.setText('Warning ! Automatic Backup Failed !!')
        self.record_activity('Logged out')
        main.close()
    def dis_buttons(self):
        self.lineEdit_37.setEnabled(False)
        self.lineEdit_52.setEnabled(False)
        self.lineEdit_68.setEnabled(False)
        self.lineEdit_67.setEnabled(False)
        self.lineEdit_53.setEnabled(False)
        self.lineEdit_69.setEnabled(False)
        self.lineEdit_70.setEnabled(False)
        self.groupBox_7.setEnabled(False)
        self.groupBox_8.setEnabled(False)
        self.groupBox_9.setEnabled(False)
        self.groupBox_40.setEnabled(True)

    def key_events(self):
        self.lineEdit_77.returnPressed.connect(self.change_password)
        self.lineEdit_78.returnPressed.connect(self.change_password)
        self.lineEdit_66.returnPressed.connect(self.add_user)
        self.lineEdit_71.returnPressed.connect(self.add_user)
        self.lineEdit_72.returnPressed.connect(self.add_user)
        self.lineEdit_73.returnPressed.connect(self.add_user)
        self.lineEdit_74.returnPressed.connect(self.add_user)
        self.lineEdit_76.returnPressed.connect(self.delete_user)
        self.lineEdit_3.returnPressed.connect(self.add_customer)
        self.lineEdit_14.returnPressed.connect(self.add_customer)
        self.lineEdit_17.returnPressed.connect(self.add_customer)
        self.lineEdit_18.returnPressed.connect(self.add_customer)
        self.lineEdit.returnPressed.connect(self.work_sheet_check)
        self.lineEdit_4.returnPressed.connect(self.cal_interest)
        self.lineEdit_10.returnPressed.connect(self.total)
        self.lineEdit_11.returnPressed.connect(self.total)
        self.lineEdit_13.returnPressed.connect(self.total)
        self.lineEdit_64.returnPressed.connect(self.set_receipt)
        self.lineEdit_55.returnPressed.connect(self.receipt_total)
        self.lineEdit_56.returnPressed.connect(self.receipt_total)
        self.lineEdit_57.returnPressed.connect(self.receipt_total)
        self.lineEdit_58.returnPressed.connect(self.receipt_total)
        self.lineEdit_59.returnPressed.connect(self.receipt_total)
        self.lineEdit_61.returnPressed.connect(self.receipt_total)
        self.lineEdit_75.returnPressed.connect(self.receipt_total)
        self.lineEdit_43.returnPressed.connect(self.deb_card_fill)
        self.lineEdit_20.returnPressed.connect(self.search)
        self.lineEdit_27.returnPressed.connect(self.cancel)
        self.lineEdit_28.returnPressed.connect(self.confirm_cancel)
        self.lineEdit_29.returnPressed.connect(self.confirm_cancel)
        self.lineEdit_30.returnPressed.connect(self.delete_loan)
        self.lineEdit_31.returnPressed.connect(self.delete_loan)
        self.lineEdit_51.returnPressed.connect(self.delete_loan)
        self.lineEdit_21.returnPressed.connect(self.add_voucher)
        self.lineEdit_22.returnPressed.connect(self.add_voucher)
        self.lineEdit_24.returnPressed.connect(self.add_voucher)
        self.lineEdit_25.returnPressed.connect(self.add_voucher)
        self.lineEdit_8.returnPressed.connect(self.set_installment)
        self.lineEdit_7.returnPressed.connect(self.set_installment_again)
        self.lineEdit_91.returnPressed.connect(self.load_receipt)
        self.lineEdit_92.returnPressed.connect(self.delete_receipt)
        self.lineEdit_93.returnPressed.connect(self.delete_receipt)
        
        
        
        
        
        
        
        

        
        
        





























class login(QtGui.QMainWindow, form_class2):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.check)
        self.lineEdit.returnPressed.connect(self.check)
        self.lineEdit_2.returnPressed.connect(self.check)
    def check(self):
        global un,pw
        self.label_5.setText('')
        conn = sqlite3.connect('main.db')
        c=conn.cursor()
        un=self.lineEdit.text()
        c.execute("select `password` from users where `username`='%s'"%(un))
        pw=c.fetchone()
        if pw and pw[0]==hashlib.md5(str(self.lineEdit_2.text())).hexdigest():
            c.execute("insert into logins(username,date,time,state) values('%s','%s','%s','Logged in')"%(un,str(datetime.datetime.now()).split()[0],str(datetime.datetime.now()).split()[1]))
            conn.commit()
            loginWindow.close()
            main.show()
        else:
            self.label_5.setText('Wrong Username or Password')
            self.lineEdit_2.setText('')
app = QtGui.QApplication(sys.argv)
loginWindow = login(None)
loginWindow.show()
main=MyWindowClass(None)
ret=app.exec_()
sys.exit(ret)
