# Core Pkgs
import streamlit as st

# EDA Pkgs
import pandas as pd

# Description: This program detects if someone has diabetes using machine learning and python!

# Import the libraries

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from PIL import Image


# For Hashing Passwords
import hashlib

import sqlite3

#Admin Database
conn = sqlite3.connect('DbAdmin.db')
c = conn.cursor()

#Doctor Database
conn1 = sqlite3.connect('DbDoctor.db')
c1 = conn1.cursor()


#Under Admin
def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(firstname TEXT, lastname TEXT, gender TEXT, age TEXT,location TEXT, contact TEXT,username TEXT,password TEXT)')

def add_userdata(firstname,lastname,gender,age,location,contact,username,password):
    c.execute('INSERT INTO userstable(firstname,lastname,gender,age,location,contact,username,password) VALUES (?,?,?,?,?,?,?,?)',(firstname,lastname,gender,age,location,contact,username,password))
    conn.commit()

#Under Doctor
def create_usertable1():
    c1.execute('CREATE TABLE IF NOT EXISTS userstable1(glucose TEXT,blood_pressure TEXT,insulin TEXT,bmi TEXT,age TEXT, doctor TEXT, timeslot1 TEXT, timeslot2 TEXT,contact TEXT)')

def add_userdata1(glucose,blood_pressure,insulin,bmi,age,doctor,timeslot1,timeslot2,contact):
    c1.execute('INSERT INTO userstable1(glucose,blood_pressure,insulin,bmi,age,doctor,timeslot1,timeslot2,contact) VALUES (?,?,?,?,?,?,?,?,?)',(glucose,blood_pressure,insulin,bmi,age,doctor,timeslot1,timeslot2,contact))
    conn1.commit()


#Login Same for Admin And Doctor
def login_user(username,password):
    c.execute('SELECT * FROM userstable WHERE username = ? AND password = ?',(username,password))
    data = c.fetchall()
    return data

#def login_user(username,password):
    #c.execute("SELECT * FROM userstable WHERE username = '%s'AND password = '%s'"),(username,password)
    #data = c.fetchall()
    #return data

#Admin View
def view_all_users1():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data

#Doctor View
def view_all_users2():
    c1.execute('SELECT * FROM userstable1')
    data = c1.fetchall()
    return data


# Password
#def generate_hashes(password):
    #return hashlib.sha256(str.encode(password)).hexdigest()

#def verify_hashes(password,hashed_text):
    #if generate_hashes(password) == hashed_text:
        #return hashed_text
    #return False


def main():
    """Simple Login App"""

st.title("ONE-STOP DIABETES DISEASE SOLUTION USING MACHINE LEARNING")
st.subheader("")

menu = ["Home","Admin Login","Doctor Login","User Login","SignUp"]


choice = st.sidebar.selectbox("Menu",menu)

if choice == "Home":
    # Open and display an image
    #st.title("ONE-STOP DIABETES DISEASE SOLUTION USING MACHINE LEARNING")
    #st.subheader("")
    image = Image.open('C:/Users/yadav/PycharmProjects/Major Project/Diabetes prediction Webapp.jpg')
    st.image(image, caption='ML', use_column_width=True)
    st.header("Home")
    st.write("Machine Learning techniques (MLT) are used to predict medical datasets at an early stage of safe human life. Currently Diabetes Diseases are among the "
             "leading cause of death in the world. ")
    st.header("About Diabetes Disease")
    st.write("Diabetes is chronic disease with the potential to cause a worldwide health care crisis.Type 1 and type 2 diabetes"
             "are the most common forms of the disease, but there are also other kinds, such as gestational diabetes, which occurs during pregnancy, as well as other" 
             "forms. However, early prediction of diabetes is quite challenging task for medical practitioners due to complex interdependence on various factors as "
             "diabetes affects human organs such as kidney, eye, heart, nerves, foot etc. systems aimed to identify diabetes by increasing the accuracy of prediction"
             "rate. ")
    st.header("Types of Diabetes Disease")
    st.subheader("Type 1 Diabetes")
    st.write("Type 1 Diabetes is an autoimmune condition. It happens when your body attecks your pancreas with antibodies. The organ is damaged and doesn't make insulin.")
    st.write("Your genes might cause this type of diabetes. It could also happen because of problems with cells in your pancreas that make insulin.")
    st.write("Many of the health problems that can come with type 1 happen because of damage of tiny blood vessels in your eyes(called diabetic retinopathy),"
             " nerves(diabetic neuropathy), and kidneys(diabetic nephropathy). People with type 1 also have a higher risk of heart disease and stroke.")
    st.write("Treatment for type 1 diabetes involves injecting insulin into the fatty tissue just under your skin. You might use:")
    st.write("-Syringes")
    st.write("-Insulin pens that use prefilled cartridges and a thin needle")
    st.write("-Jet injectors that use high-pressure air to send a spray of insulin through the skin")
    st.write("-Pumps that send insulin through a tube to a catheter under the skin of your belly")


    st.subheader("Type 2 Diabetes")
    st.write("Type 2 Diabetes used to be called non-insulin-dependent or adult-onset diabetes. But it's become more common in children and teens over the past 20 years,"
             " largely bacause more young people are overweight or obese. About 90% of people with daibetes have type 2.")
    st.write("When you have type 2 daibetes, your pancreas usually creates some insulin. But either it's not enough or your body doesn't use it like it should. Insulin resistance, "
             "when your cells don't respond to insulin, usually happens in fat, and muscle cells.")
    st.write("Type 2 daibetes is often milder than type 1. But it can still cause major health complications, especially in the tiny blood vessels in your kidneys, nerves, and eyes."
             " Type 2 also raises your risk of heart disease and stroke.")
    st.write("Treatment for type 2 daibetes involves keeping a healthy weight, eating right, and exercising. Some people need medication, too.")
    st.subheader("Gestational Diabetes")
    st.write("Pregnancy usually causes some form of insulin resistance. If this becomes diabetes, it's called gestational."
             " Doctors often spot it in middle or late pregnancy. Because a woman's blood sugars travel through their placenta to the baby, it;'s important to control gestational diabetes"
             " to protect the baby's growth and development.")
    st.write("Doctors report gestational diabetes in 2% to 10% of pregnancies. It usually goes away after birth. But up to 10% of women who have gestational diabetes get type 2, weeks or "
             "even years later. It is more risk for the baby than the mother. A baby might have unusual weight gain before birth, trouble breathing at birth, or a higher risk of obesity and diabetes later in lige.")
    st.write("Gestational diabetes treatment involves:")
    st.write("-Careful meal planning to make sure you get enough nutrients without too much fat and calories")
    st.write("-Daily exercise")
    st.write("-Keeping weight gain under control")
    st.write("-taking insulin to control your blood sugar levels, if needed.")
    st.subheader("Other Forms of Diabetes")
    st.write("In 1% to 5% of people who have diabetes, other conditions might be the cause. These include diseases of the pancreas, certain surgeries and medications, and infections. In these cases,"
             " your doctor might want to keep an eye on your blood sugar levels.")





#Admin Login

elif choice == "Admin Login":
    st.subheader("Admin Section")
    username = st.sidebar.text_input("User Name")
    password = st.sidebar.text_input("Password", type='password')
    if st.sidebar.checkbox("Login"):
        # if password == '12345':
        create_usertable()
        #hashed_pswd = generate_hashes(password)
        #result = login_user(username, verify_hashes(password, hashed_pswd))
        result = login_user(username,password)
        if result:

            st.success("Logged in as {}".format(username))

            task = st.selectbox("Task",["Profiles"])
            st.subheader("User Profiles")
            user_result = view_all_users1()
            clean_db = pd.DataFrame(user_result, columns=["Firstname","Lastname","Gender","Age","Location","Contact","Username", "Password"])
            st.dataframe(clean_db)

        else:
            st.warning("Incorrect Username/Password!")

#Doctor Login
elif choice == "Doctor Login":
    st.subheader("Doctor Section")
    username = st.sidebar.text_input("User Name")
    password = st.sidebar.text_input("Password", type='password')
    if st.sidebar.checkbox("Login"):
        # if password == '12345':
        create_usertable()
        #hashed_pswd = generate_hashes(password)
        #result = login_user(username, verify_hashes(password, hashed_pswd))
        result = login_user(username,password)
        if result:

            st.success("Logged in as {}".format(username))

            task = st.selectbox("Task",["Profiles"])
            st.subheader("Patient Profiles")
            user_result = view_all_users2()
            clean_db = pd.DataFrame(user_result, columns=["UD1-Glucose","UD2-Blood Pressure","UD3-Insulin","UD4-BMI","UD5-Age","Doctor Selected","Date","Time","Contact"])
            st.dataframe(clean_db)

        else:
            st.warning("Incorrect Username/Password!")




#User Login

if choice == "User Login":
    st.subheader("Login Section")

    username = st.sidebar.text_input("User Name")
    password = st.sidebar.text_input("Password",type='password')
    if st.sidebar.checkbox("Login"):
        #if password == '12345':
        create_usertable()
        #hashed_pswd = generate_hashes(password)
        #result = login_user(username,verify_hashes(password,hashed_pswd))
        result = login_user(username,password)
        if result:

            st.success("Logged in as {}".format(username))

            task = st.selectbox("Task",["Predict Chances of Diabetes","Prediction with Medical Data","Contact with Doctor"])

            # Predict chances of diabetes disease

            if task == "Predict Chances of Diabetes":
                st.subheader("Please input the symptoms you are facing !")

                first=st.radio("Do you feel very tired doing little amount of work?",("Yes","No"))
                second=st.radio("Do you urinate alot, often at night?", ("Yes", "No"))
                third=st.radio("Do you have some signs of blurry vision?", ("Yes", "No"))
                fourth=st.radio("Are you loosing weight without trying?", ("Yes", "No"))
                fifth=st.radio("Do you feel hungry most of the time?", ("Yes", "No"))
                sixth=st.radio("Do you have numb or tingling hands or feet?", ("Yes", "No"))

                if st.button("Submit"):

                    if first == 'Yes' and second == 'Yes' and third == 'Yes' and fourth == 'Yes' and fifth == 'Yes' and sixth == 'Yes':
                        st.warning("You may have chances of of having Daibetes Disease.")

                        st.write("")
                        st.write("*If you have your medical data ready than check more about the disease in our 'Prediction Portal'.")
                        st.write("*If not then you can first get your medical data ready through a pathology center and can check here more about your disease before visiting your doctor. So that you have some knowledge about your health. ")
                        st.write("Thank You!")

                    elif first == 'Yes' and second == 'No' and third == 'No' and fourth == 'No' and fifth == 'No' and sixth == 'No':
                            st.success("You have no chances of Diabetes Disease. Cheers!")


                    elif first == 'Yes' and second == 'Yes' and third == 'No' and fourth == 'No' and fifth == 'No' and sixth == 'No':
                        st.success("You have no chances of Diabetes Disease. Cheers!")

                    elif first == 'Yes' and second == 'Yes' and third == 'Yes' and fourth == 'No' and fifth == 'No' and sixth == 'No':
                        st.warning("You may have chances of of having Daibetes Disease.")

                        st.write("")
                        st.write("*If you have your medical data ready than check more about the disease in our prediction portal.")
                        st.write("*If not then you can first get your medical data ready through a pathology center and can check here more about your disease before visiting your doctor. So that you have some knowledge about your health. ")
                        st.write("Thank You!")

                    elif first == 'Yes' and second == 'Yes' and third == 'Yes' and fourth == 'Yes' and fifth == 'No' and sixth == 'No':
                        st.warning("You may have chances of of having Daibetes Disease.")

                        st.write("")
                        st.write("*If you have your medical data ready than check more about the disease in our prediction portal.")
                        st.write("*If not then you can first get your medical data ready through a pathology center and can check here more about your disease before visiting your doctor. So that you have some knowledge about your health. ")
                        st.write("Thank You!")

                    elif first == 'Yes' and second == 'Yes' and third == 'Yes' and fourth == 'Yes' and fifth == 'Yes' and sixth == 'No':
                        st.warning("You may have chances of of having Daibetes Disease.")

                        st.write("")
                        st.write("*If you have your medical data ready than check more about the disease in our prediction portal.")
                        st.write("*If not then you can first get your medical data ready through a pathology center and can check here more about your disease before visiting your doctor. So that you have some knowledge about your health. ")
                        st.write("Thank You!")

                    elif first == 'No' and second == 'Yes' and third == 'Yes' and fourth == 'Yes' and fifth == 'Yes' and sixth == 'Yes':
                        st.warning("You may have chances of of having Daibetes Disease.")

                        st.write("")
                        st.write("*If you have your medical data ready than check more about the disease in our prediction portal.")
                        st.write("*If not then you can first get your medical data ready through a pathology center and can check here more about your disease before visiting your doctor. So that you have some knowledge about your health. ")
                        st.write("Thank You!")

                    elif first == 'No' and second == 'No' and third == 'Yes' and fourth == 'Yes' and fifth == 'Yes' and sixth == 'Yes':
                        st.success("You have no chances of Diabetes Disease. Cheers!")

                    elif first == 'No' and second == 'No' and third == 'No' and fourth == 'Yes' and fifth == 'Yes' and sixth == 'Yes':
                        st.success("You have no chances of Diabetes Disease. Cheers!")

                    elif first == 'No' and second == 'No' and third == 'No' and fourth == 'No' and fifth == 'Yes' and sixth == 'Yes':
                        st.success("You have no chances of Diabetes Disease. Cheers!")

                    elif first == 'No' and second == 'No' and third == 'No' and fourth == 'No' and fifth == 'No' and sixth == 'Yes':
                        st.success("You have no chances of Diabetes Disease. Cheers!")

                    elif first == 'Yes' and second == 'No' and third == 'No' and fourth == 'No' and fifth == 'No' and sixth == 'Yes':
                        st.success("You have no chances of Diabetes Disease. Cheers!")

                    elif first == 'Yes' and second == 'No' and third == 'Yes' and fourth == 'No' and fifth == 'Yes' and sixth == 'No':
                        st.success("You have no chances of Diabetes Disease. Cheers!")

                    elif first == 'Yes' and second == 'Yes' and third == 'No' and fourth == 'No' and fifth == 'Yes' and sixth == 'Yes':
                        st.warning("You may have chances of of having Daibetes Disease.")

                        st.write("")
                        st.write("*If you have your medical data ready than check more about the disease in our prediction portal.")
                        st.write("*If not then you can first get your medical data ready through a pathology center and can check here more about your disease before visiting your doctor. So that you have some knowledge about your health. ")
                        st.write("Thank You!")

                    elif first == 'Yes' and second == 'No' and third == 'Yes' and fourth == 'Yes' and fifth == 'Yes' and sixth == 'Yes':
                        st.warning("You may have chances of of having Daibetes Disease.")

                        st.write("")
                        st.write("*If you have your medical data ready than check more about the disease in our prediction portal.")
                        st.write("*If not then you can first get your medical data ready through a pathology center and can check here more about your disease before visiting your doctor. So that you have some knowledge about your health. ")
                        st.write("Thank You!")

                    elif first == 'Yes' and second == 'No' and third == 'No' and fourth == 'Yes' and fifth == 'Yes' and sixth == 'Yes':
                        st.success("You have no chances of Diabetes Disease. Cheers!")

                    elif first == 'Yes' and second == 'No' and third == 'No' and fourth == 'No' and fifth == 'Yes' and sixth == 'Yes':
                        st.success("You have no chances of Diabetes Disease. Cheers!")

                    elif first == 'Yes' and second == 'Yes' and third == 'No' and fourth == 'No' and fifth == 'Yes' and sixth == 'Yes':
                        st.warning("You may have chances of of having Daibetes Disease.")

                        st.write("")
                        st.write("*If you have your medical data ready than check more about the disease in our prediction portal.")
                        st.write("*If not then you can first get your medical data ready through a pathology center and can check here more about your disease before visiting your doctor. So that you have some knowledge about your health. ")
                        st.write("Thank You!")

                    elif first == 'Yes' and second == 'Yes' and third == 'No' and fourth == 'Yes' and fifth == 'Yes' and sixth == 'No':
                        st.warning("You may have chances of of having Daibetes Disease.")

                        st.write("")
                        st.write("*If you have your medical data ready than check more about the disease in our prediction portal.")
                        st.write("*If not then you can first get your medical data ready through a pathology center and can check here more about your disease before visiting your doctor. So that you have some knowledge about your health. ")
                        st.write("Thank You!")

                    elif first == 'Yes' and second == 'No' and third == 'No' and fourth == 'Yes' and fifth == 'No' and sixth == 'Yes':
                        st.success("You have no chances of Diabetes Disease. Cheers!")

                    elif first == 'Yes' and second == 'No' and third == 'Yes' and fourth == 'No' and fifth == 'No' and sixth == 'Yes':
                        st.success("You have no chances of Diabetes Disease. Cheers!")

                    elif first == 'Yes' and second == 'No' and third == 'Yes' and fourth == 'No' and fifth == 'No' and sixth == 'No':
                        st.success("You have no chances of Diabetes Disease. Cheers!")

                    elif first == 'Yes' and second == 'No' and third == 'Yes' and fourth == 'Yes' and fifth == 'Yes' and sixth == 'No':
                        st.warning("You may have chances of of having Daibetes Disease.")

                        st.write("")
                        st.write("*If you have your medical data ready than check more about the disease in our prediction portal.")
                        st.write("*If not then you can first get your medical data ready through a pathology center and can check here more about your disease before visiting your doctor. So that you have some knowledge about your health. ")
                        st.write("Thank You!")

                    elif first == 'Yes' and second == 'Yes' and third == 'No' and fourth == 'Yes' and fifth == 'No' and sixth == 'Yes':
                        st.warning("You may have chances of of having Daibetes Disease.")

                        st.write("")
                        st.write("*If you have your medical data ready than check more about the disease in our prediction portal.")
                        st.write("*If not then you can first get your medical data ready through a pathology center and can check here more about your disease before visiting your doctor. So that you have some knowledge about your health. ")
                        st.write("Thank You!")

                    elif first == 'Yes' and second == 'Yes' and third == 'Yes' and fourth == 'No' and fifth == 'Yes' and sixth == 'No':
                        st.warning("You may have chances of of having Daibetes Disease.")

                        st.write("")
                        st.write("*If you have your medical data ready than check more about the disease in our prediction portal.")
                        st.write("*If not then you can first get your medical data ready through a pathology center and can check here more about your disease before visiting your doctor. So that you have some knowledge about your health. ")
                        st.write("Thank You!")

                    elif first == 'Yes' and second == 'Yes' and third == 'Yes' and fourth == 'No' and fifth == 'No' and sixth == 'Yes':
                        st.warning("You may have chances of of having Daibetes Disease.")

                        st.write("")
                        st.write("*If you have your medical data ready than check more about the disease in our prediction portal.")
                        st.write("*If not then you can first get your medical data ready through a pathology center and can check here more about your disease before visiting your doctor. So that you have some knowledge about your health. ")
                        st.write("Thank You!")

                    elif first == 'Yes' and second == 'Yes' and third == 'No' and fourth == 'No' and fifth == 'NO' and sixth == 'Yes':
                        st.warning("You may have chances of of having Daibetes Disease.")

                        st.write("")
                        st.write("*If you have your medical data ready than check more about the disease in our prediction portal.")
                        st.write("*If not then you can first get your medical data ready through a pathology center and can check here more about your disease before visiting your doctor. So that you have some knowledge about your health. ")
                        st.write("Thank You!")


                    elif first == 'Yes' and second == 'No' and third == 'No' and fourth == 'Yes' and fifth == 'No' and sixth == 'Yes':
                        st.success("You have no chances of Diabetes Disease. Cheers!")


                    elif first == 'Yes' and second == 'No' and third == 'Yes' and fourth == 'Yes' and fifth == 'No' and sixth == 'Yes':
                        st.warning("You may have chances of of having Daibetes Disease.")

                        st.write("")
                        st.write("*If you have your medical data ready than check more about the disease in our prediction portal.")
                        st.write("*If not then you can first get your medical data ready through a pathology center and can check here more about your disease before visiting your doctor. So that you have some knowledge about your health. ")
                        st.write("Thank You!")

                    elif first == 'Yes' and second == 'Yes' and third == 'Yes' and fourth == 'No' and fifth == 'Yes' and sixth == 'Yes':
                        st.warning("You may have chances of of having Daibetes Disease.")

                        st.write("")
                        st.write("*If you have your medical data ready than check more about the disease in our prediction portal.")
                        st.write("*If not then you can first get your medical data ready through a pathology center and can check here more about your disease before visiting your doctor. So that you have some knowledge about your health. ")
                        st.write("Thank You!")

                    elif first == 'Yes' and second == 'Yes' and third == 'Yes' and fourth == 'Yes' and fifth == 'No' and sixth == 'Yes':
                        st.warning("You may have chances of of having Daibetes Disease.")

                        st.write("")
                        st.write("*If you have your medical data ready than check more about the disease in our prediction portal.")
                        st.write("*If not then you can first get your medical data ready through a pathology center and can check here more about your disease before visiting your doctor. So that you have some knowledge about your health. ")
                        st.write("Thank You!")

                    elif first == 'Yes' and second == 'Yes' and third == 'No' and fourth == 'No' and fifth == 'Yes' and sixth == 'No':
                        st.warning("You may have chances of of having Daibetes Disease.")

                        st.write("")
                        st.write("*If you have your medical data ready than check more about the disease in our prediction portal.")
                        st.write("*If not then you can first get your medical data ready through a pathology center and can check here more about your disease before visiting your doctor. So that you have some knowledge about your health. ")
                        st.write("Thank You!")

                    elif first == 'Yes' and second == 'No' and third == 'No' and fourth == 'No' and fifth == 'Yes' and sixth == 'No':
                        st.success("You have no chances of Diabetes Disease. Cheers!")

                    elif first == 'Yes' and second == 'Yes' and third == 'No' and fourth == 'Yes' and fifth == 'No' and sixth == 'No':
                        st.warning("You may have chances of of having Daibetes Disease.")

                        st.write("")
                        st.write("*If you have your medical data ready than check more about the disease in our prediction portal.")
                        st.write("*If not then you can first get your medical data ready through a pathology center and can check here more about your disease before visiting your doctor. So that you have some knowledge about your health. ")
                        st.write("Thank You!")

                    elif first == 'Yes' and second == 'Yes' and third == 'No' and fourth == 'Yes' and fifth == 'Yes' and sixth == 'Yes':
                        st.warning("You may have chances of of having Daibetes Disease.")

                        st.write("")
                        st.write("*If you have your medical data ready than check more about the disease in our prediction portal.")
                        st.write("*If not then you can first get your medical data ready through a pathology center and can check here more about your disease before visiting your doctor. So that you have some knowledge about your health. ")
                        st.write("Thank You!")

                    elif first == 'No' and second == 'Yes' and third == 'No' and fourth == 'Yes' and fifth == 'Yes' and sixth == 'No':
                        st.warning("You may have chances of of having Daibetes Disease.")

                        st.write("")
                        st.write("*If you have your medical data ready than check more about the disease in our prediction portal.")
                        st.write("*If not then you can first get your medical data ready through a pathology center and can check here more about your disease before visiting your doctor. So that you have some knowledge about your health. ")
                        st.write("Thank You!")

                    elif first == 'Yes' and second == 'No' and third == 'No' and fourth == 'Yes' and fifth == 'Yes' and sixth == 'No':
                        st.warning("You may have chances of of having Daibetes Disease.")

                        st.write("")
                        st.write("*If you have your medical data ready than check more about the disease in our prediction portal.")
                        st.write("*If not then you can first get your medical data ready through a pathology center and can check here more about your disease before visiting your doctor. So that you have some knowledge about your health. ")
                        st.write("Thank You!")



                    elif first == 'Yes' and second == 'No' and third == 'Yes' and fourth == 'Yes' and fifth == 'No' and sixth == 'No':
                        st.success("You have no chances of Diabetes Disease. Cheers!")

                    elif first == 'No' and second == 'Yes' and third == 'No' and fourth == 'Yes' and fifth == 'No' and sixth == 'Yes':
                        st.warning("You may have chances of of having Daibetes Disease.")

                        st.write("")
                        st.write("*If you have your medical data ready than check more about the disease in our prediction portal.")
                        st.write("*If not then you can first get your medical data ready through a pathology center and can check here more about your disease before visiting your doctor. So that you have some knowledge about your health. ")
                        st.write("Thank You!")

                    elif first == 'No' and second == 'No' and third == 'Yes' and fourth == 'Yes' and fifth == 'No' and sixth == 'Yes':
                        st.success("You have no chances of Diabetes Disease. Cheers!")






                    elif first == 'No' and second == 'No' and third == 'No' and fourth == 'No' and fifth == 'No' and sixth == 'No':
                        st.success("You have no chances of Diabetes Disease. Cheers!")




            elif task == "Prediction with Medical Data":
                st.subheader("Enter the Values in the sidebar to check your result !")


                feature_names = ['glucose', 'blood_pressure','insulin', 'bmi', 'dpf','age']

                df = pd.read_csv('C:/Users/yadav/PycharmProjects/Major Project/diabetes1.csv')

                # Set a subheader
                #st.subheader('Data Information:')

                # Show the data as a table
                #st.dataframe(df)

                #Show statistics on the data
                st.write(df.describe())

                # Set the data as a chart
                #chart = st.bar_chart(df)

                # Split the data into independent 'X' and independent 'Y' variables
                X = df.iloc[:, 0:6].values
                Y = df.iloc[:, -1].values

                # Split the data set into 75% Training and 25% Testing
                X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=0)


                # Fet the feature input from the user
                def get_user_input():
                    st.sidebar.header("Enter Your Inputs")
                    #pregnancies = st.sidebar.slider('pregnancies', 0, 17, 3)
                    glucose = st.sidebar.slider('Glucose', 0, 199, 117)
                    blood_pressure = st.sidebar.slider('Blood Pressure', 0, 122, 72)
                    #skin_thickness = st.sidebar.slider('skin_thickness', 0, 99, 23)
                    insulin = st.sidebar.slider('Insulin', 0.0, 846.0, 30.0)
                    bmi = st.sidebar.slider('BMI (Body Mass Index)', 0.0, 67.1, 32.0)
                    dpf = st.sidebar.slider('DPF (Diabetes Pedigree Function)', 0.078, 2.42, 0.3725)
                    age = st.sidebar.slider('Age', 21, 81, 29)

                    # Store a dictionary into a variable
                    user_data = {#'pregnancies': pregnancies,
                                 'glucose': glucose,
                                 'blood_pressure': blood_pressure,
                                 #'skin_thickness': skin_thickness,
                                 'insulin': insulin,
                                 'bmi': bmi,
                                 'dpf': dpf,
                                 'age': age
                                 }

                    # Tranform the data into a data frame
                    features = pd.DataFrame(user_data, index=[0])
                    return features


                # Store the user input into a variable
                user_input = get_user_input()

                # Set a subheader and display the users input
                st.subheader('User Input:')
                st.write(user_input)

                # Create and train the model
                RandomForestClassifier = RandomForestClassifier()
                RandomForestClassifier.fit(X_train, Y_train)

                # Show the model metrics
                st.subheader('Model Test Accuracy Score:')
                st.write(str(accuracy_score(Y_test, RandomForestClassifier.predict(X_test)) * 100) + '%')

                # Store the models predictions in a variable
                prediction = RandomForestClassifier.predict(user_input)

                # Set a subheader and display the classification
                st.subheader('Your Result:')
                st.write(prediction)
                if prediction == 1 :
                     st.warning("Patient Suffers from Diabetes Disease.")
                     st.warning("Please get checked from a Doctor soon!")

                     st.warning("Type-1 Diabetes Disease")
                     st.write("")
                     st.subheader("Precautions for Type-1 Daibetes")
                     #st.write("1. Make a commitment to managing your diabetes")
                     st.write("1. Don't smoke")
                     st.write("2. Keep your blood pressure and cholestrol under control")
                     st.write("3. Schedule regular physicals and eye exams")
                     #st.write("5. Keep your vaccines up to date")
                     #st.write("6. Take care of your teeth")
                     #st.write("7. Pay attention to your feet")
                     st.write("4. If you drink alcohol, do so responsibly")
                     st.write("5. Manage your stress")
                     #st.write("10. Follow a very-low-carb diet")
                     st.write("")
                     st.subheader("Treatment for Type-1 Diabetes")
                     st.write("Treatment for type 1 diabetes involves injecting insulin into the fatty tissue just under your skin. You might use:")
                     st.write("-Syringes")
                     st.write("-Insulin pens that use prefilled cartridges and a thin needle")
                     #st.write("-Jet injectors that use high-pressure air to send a spray of insulin through the skin")
                     st.write("-Pumps that send insulin through a tube to a catheter under the skin of your belly")
                     st.write("")
                     st.subheader("Diet Plan for Type-1 Daibetes")

                     image = Image.open('C:/Users/yadav/PycharmProjects/Major Project/diet chart.PNG')
                     st.image(image, caption='Diet Plan', use_column_width=True)
                     href = f'<a href = "https://emoha.com/blogs/health/indian-diet-for-diabetic-patients">For a detailed diet plan click here to know more!!</a>'
                     st.markdown(href,unsafe_allow_html=True)

                else:
                    st.success("Patient does not suffer from Diabetes Disease.")
                    st.success("Cheers! Stay Healthy!")



            elif task == "Contact with Doctor":
                st.subheader("Get Your Queries Solved!")
                st.write("Given below are the contact details of the doctor that can solve your doubts regarding your test results that you got through our WebApp.")
                st.write("")
                st.subheader("Doctor Details:")
                st.write("For Male patients:")
                st.write("*Dr. Punit Dahiya -------(Call Time - 4pm to 6pm--/--Mon-Fri)")
                st.write("*Dr. Rahul Sharma -------(Call Time - 4pm to 6pm--/--Mon-Fri)")
                st.write("*Dr. Aniket Parikh -------(Call Time - 4pm to 6pm--/--Mon-Fri)")
                st.write("")
                st.write("For Female patients:")
                st.write("*Dr. Suresh Dixit -------(Call Time - 4pm to 6pm--/--Mon-Fri)")
                st.write("")
                st.subheader("Enter Your Details Below")
                st.write("")

                st.write('User Medical Input:')
                glucose = st.text_input("Glucose")
                blood_pressure = st.text_input("Blood Pessure")
                insulin = st.text_input("Insulin")
                bmi = st.text_input("BMI")
                age = st.text_input("Age")


                doctor = st.selectbox("Select Doctor",("Doctor Punit Dahiya","Doctor Rahul Sharma","Doctor Aniket Parikh","Doctor Suresh Dixit"))
                st.write("You selected this option --",doctor)
                st.info("Contact via call. Please select Date and Time.")
                timeslot1 = st.text_input("Enter Date---(Sat-Sun Closed)","DD-MM-YYYY")
                st.write("You selected this date --", timeslot1)
                timeslot2 = st.selectbox("Select Time", ("4:00 PM", "4:15 PM","4:30 PM","4:45 PM","5:00 PM","5:15 PM","5:30 PM","5:45 PM","6:00 PM"))
                st.write("You selected this option --", timeslot2)
                contact = st.text_input("Enter Your Contact")

                if st.button("Submit"):
                    create_usertable1()
                    # hashed_new_password = generate_hashes(new_password)
                    #add_userdata(user_input,doctor,timeslot1,timeslot2,contact)
                    add_userdata1(glucose,blood_pressure,insulin,bmi,age,doctor,timeslot1,timeslot2,contact)
                    st.success("Thank You for submitting your contact information.")
                    st.success("You will be soon contacted by our doctor representative at your scheduled time.")





        else:
            st.warning("Incorrect Username/Password!")



elif choice == "SignUp":
    st.subheader("Create New Account")
    new_firstname = st.text_input("Enter Your Firstname")
    new_lastname = st.text_input("Enter Your Lastname")
    new_gender = st.radio("Select Your Gender", ("Male", "Female", "Transgender"))
    new_age = st.text_input("Enter Your Age")
    new_location = st.text_input("Enter Your Location")
    new_contact = st.text_input("Enter Your Contact")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password",type='password')
    confirm_password = st.text_input("Confirm Password",type='password')
    if new_password == confirm_password:
        st.success("Password Confirmed.")
    else:
        st.warning("Passwords not the same.")


    if st.button("SignUp"):
        create_usertable()
        #hashed_new_password = generate_hashes(new_password)
        add_userdata(new_firstname,new_lastname,new_gender,new_age,new_location,new_contact,new_user,new_password)
        st.success("You have successfully created a valid account.")
        st.info("Go to Login Menu to get started.")






if __name__ == '__main__':
    main()