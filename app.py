import flask
import pickle
import pandas as pd
#import 'run model' from s

# Use pickle to load in the pre-trained model
with open(f'customer_satisfaction.pkl', 'rb') as f:
    model = pickle.load(f)

with open(f'repeat_customer.pkl', 'rb') as f:
    model2 = pickle.load(f)

# Initialise the Flask app
app = flask.Flask(__name__, template_folder='templates')

# Set up the main route
@app.route('/main.html', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('main.html'))

    if flask.request.method == 'POST':
        # Extract the input
        product_description_lenght = flask.request.form['product_description_lenght']
        product_photos_qty = flask.request.form['product_photos_qty']
        Is_It_Late = flask.request.form['Is_It_Late']
        Payment_Type = flask.request.form['Payment_Type']
        Total_Order_Value = flask.request.form['Total_Order_Value']

        # Make DataFrame for model
        input_variables = pd.DataFrame([[product_description_lenght, product_photos_qty, Is_It_Late, Payment_Type,
                                        Total_Order_Value]],
                                       columns=['product_description_lenght', 'product_photos_qty', 'Is_It_Late',
                                       'Payment_Type', 'Total_Order_Value'],
                                       dtype=float,
                                       index=['input'])

        # Get the model's prediction
        prediction = model.predict(input_variables)[0]

        # Convert Output to Text
        if prediction > 1:
            prediction = "Positive"
        else:
            prediction = "Negative"

        # Render the form again, but add in the prediction and remind user
        # of the values they input before
        return flask.render_template('main.html',
                                     original_input={'product_description_lenght':product_description_lenght,
                                                     'product_photos_qty':product_photos_qty,
                                                     'Is_It_Late':Is_It_Late,
                                                     'Payment_Type':Payment_Type,
                                                     'Total_Order_Value':Total_Order_Value},
                                     result=prediction,
                                     )

# Set up the main route
@app.route('/repeat-customer.html', methods=['GET', 'POST'])
def repeat():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('repeat-customer.html'))

    if flask.request.method == 'POST':
        # Extract the input
        days_early_or_late = flask.request.form['days_early_or_late']
        late = flask.request.form['late']
        review_score = flask.request.form['review_score']
        total_delivery_days = flask.request.form['total_delivery_days']

        # Make DataFrame for model
        input_variables2 = pd.DataFrame([[days_early_or_late, total_delivery_days, late, review_score]],
                                       columns=['days_early_or_late', 'total_delivery_days', 'late', 'review_score'],
                                       dtype=float,
                                       index=['input'])

        # Get the model's prediction
        prediction2 = model2.predict(input_variables2)[0]

        # Convert Output to Text
        if prediction2 > 1:
            prediction2 = "Repeat Customer"
        else:
            prediction2 = "Will Not Purchase Again"

        # Render the form again, but add in the prediction and remind user
        # of the values they input before
        return flask.render_template('repeat-customer.html',
                                     original_input={'days_early_or_late':days_early_or_late,
                                                     'total_delivery_days': total_delivery_days,
                                                     'late':late,
                                                     'review_score':review_score},
                                     result2=prediction2)

@app.route('/')
def home():
        return(flask.render_template('landing-page.html'))

@app.route('/landing-page.html')
def home2():
        return(flask.render_template('landing-page.html'))

@app.route('/tutorial.html')
def code1():
        return(flask.render_template('tutorial.html'))

@app.route('/repeat-cust-tutorial.html')
def code2():
        return(flask.render_template('repeat-cust-tutorial.html'))

@app.route('/about.html')
def about():
        return(flask.render_template('about.html'))

@app.route('/recommender-tutorial.html')
def recommender():
        return(flask.render_template('recommender-tutorial.html'))

#['days_to_delivery','late','review_score']

if __name__ == '__main__':
    app.run(debug=True)