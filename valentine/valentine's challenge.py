import pylab
import scipy
import datetime
import streamlit as st


st.title("Valentine's Challenge")

st.write("If you answer all following questions correctly, if you will get a surprise!")
submit = 0
with st.form('user_inputs'):
    singer = st.selectbox('Your Favorite Singer',options= ['Jolin','Jay','5566'])
    sport = st.selectbox('Your Favorite Sport',options= ['Volleyball','Swimming','Basketball'])
    #birth_day = st.date_input(
    # "When's your birthday",datetime.date(2019, 7, 6))
    st.form_submit_button()
    submit = submit +1

x = scipy.linspace(-2,2,1000)
y1 = scipy.sqrt(1-(abs(x)-1)**2)
y2 = -3*scipy.sqrt(1-(abs(x)/2)**0.5)
pylab.fill_between(x, y1, color='red')
pylab.fill_between(x, y2, color='red')
pylab.xlim([-2.5, 2.5])
pylab.text(0, -0.4, "Happy Valentine's Day!", fontsize=20, fontweight='bold',
           color='white', horizontalalignment='center')
pylab.savefig('heart.png')

if submit!=0:
    if singer == 'Jay' and sport == 'Basketball' :
        st.image('heart.png')
        st.balloons()
    else:
        st.write("You're wrong, please try again.")

# hear refer to the following post: https://stackoverflow.com/questions/4478078/how-to-draw-a-heart-with-pylab
