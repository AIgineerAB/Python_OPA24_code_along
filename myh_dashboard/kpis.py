from read_data import read_data

df = read_data()

#selecting rows by .query() method
#alternative is: approved = df[df["Beslut"]== "Beviljad"]
#inside the expression, we don't need to use quotation/[] to refer to a column
#inside the expression, we can use single quotation to refer to string
approved = df.query("Beslut == 'Beviljad'")

#calculate kpis
number_approved = len(approved)
total_applications = len(df)
approved_precentage = number_approved*100/total_applications




if __name__ == "__main__":
    #for testing purpose
    print(number_approved)
    print(total_applications)
    print(approved_precentage)
