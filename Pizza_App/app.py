from flask import Flask, render_template, request

app = Flask(__name__)

# Prices
PIZZA_PRICES = {'small': 10, 'medium': 15, 'large': 20}
TOPPING_PRICE = 2
DELIVERY_FEE = 3
TAX_RATE = 0.08

@app.route("/", methods=["GET", "POST"])
def index():
    receipt = None
    if request.method == "POST":
        try:
            size = request.form["size"]
            toppings = int(request.form.get("toppings", 0))
            quantity = int(request.form.get("quantity", 1))
            delivery = request.form.get("delivery", "pickup")
            
            # Calculations
            base_price = PIZZA_PRICES.get(size, 0) * quantity
            toppings_total = toppings * TOPPING_PRICE * quantity
            subtotal = base_price + toppings_total
            tax = subtotal * TAX_RATE
            delivery_fee = DELIVERY_FEE if delivery == "delivery" else 0
            total = subtotal + tax + delivery_fee
            
            # Prepare receipt
            receipt = {
                "size": size.capitalize(),
                "quantity": quantity,
                "toppings": toppings,  # Fixed typo: was "topping"
                "base_price": base_price,
                "toppings_total": toppings_total,
                "subtotal": subtotal,
                "tax": tax,
                "delivery_fee": delivery_fee,
                "total": total
            }
        except (ValueError, KeyError) as e:
            receipt = {"error": "Invalid form data"}
            
    return render_template("index.html", receipt=receipt)

if __name__ == "__main__":
    app.run(debug=True)