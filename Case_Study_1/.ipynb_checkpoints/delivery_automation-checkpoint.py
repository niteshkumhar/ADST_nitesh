def evaluate_order():
    print("=== ENTER ORDER DETAILS ===")
    
    # 1. Input Collection
    order_amount = float(input("Order Amount (INR): "))
    delivery_distance = float(input("Delivery Distance (km): "))
    customer_type = input("Customer Type (regular / gold / platinum): ").strip().lower()
    customer_rating = float(input("Customer Rating (1.0 - 5.0): "))
    restaurant_rating = float(input("Restaurant Rating (1.0 - 5.0): "))
    prep_time = int(input("Preparation Time (mins): "))
    payment_method = input("Payment Method (cod / online / wallet): ").strip().lower()
    weather = input("Weather Condition (clear / rain / storm): ").strip().lower()
    demand_level = input("Demand Level (low / medium / high): ").strip().lower()
    is_peak_hour = input("Is it Peak Hour? (yes / no): ").strip().lower() == "yes"
    prev_cancellations = int(input("Previous Cancellations count: "))


    # 2. RESTAURANT HEALTH CHECK
    if restaurant_rating < 2.5 or prep_time > 60:
        restaurant_status = "Critical (High Delays/Poor Rating)"
    elif restaurant_rating >= 4.0 and prep_time <= 30:
        restaurant_status = "Optimal (Fast & Highly Rated)"
    else:
        restaurant_status = "Standard Operations"

    # ==========================================
    # 3. CANCELLATION RISK ASSESSMENT
    # ==========================================
    if prev_cancellations >= 4 or (payment_method == "cod" and customer_rating < 3.0):
        cancellation_risk = "High"
    elif prev_cancellations >= 2 or payment_method == "cod":
        cancellation_risk = "Medium"
    else:
        cancellation_risk = "Low"

    # ==========================================
    # 4. ORDER ACCEPTANCE & MANUAL REVIEW LOGIC
    # ==========================================
    manual_review = False
    
    # Extreme Rejection Scenarios
    if weather == "storm" or delivery_distance > 25.0:
        order_status = "Rejected"
        rejection_reason = "Unsafe weather conditions or distance exceeds maximum limit (25km)."
    elif cancellation_risk == "High" and payment_method == "cod" and order_amount > 1500:
        order_status = "Rejected"
        rejection_reason = "High cancellation risk with large COD amount."
    elif restaurant_status.startswith("Critical") and demand_level == "high":
        order_status = "Rejected"
        rejection_reason = "Restaurant overwhelmed during high platform demand."
    else:
        # Check if Manual Review is needed
        if (order_amount > 5000 and payment_method == "cod") or (prev_cancellations >= 3 and cancellation_risk != "High"):
            order_status = "Manual Review Required"
            manual_review = True
        elif customer_rating < 2.0 or restaurant_rating < 3.0:
            order_status = "Manual Review Required"
            manual_review = True
        else:
            order_status = "Accepted"

    # ==========================================
    # 5. DELIVERY CHARGE CALCULATION
    # ==========================================
    # Base distance charge
    if delivery_distance <= 3:
        base_delivery = 25.0
    elif delivery_distance <= 7:
        base_delivery = 45.0
    elif delivery_distance <= 15:
        base_delivery = 80.0
    else:
        base_delivery = 120.0

    # Surge & Weather modifiers
    surge_multiplier = 1.0
    if weather == "rain":
        surge_multiplier += 0.35
    
    if demand_level == "high" and is_peak_hour:
        surge_multiplier += 0.40
    elif demand_level == "high" or is_peak_hour:
        surge_multiplier += 0.20

    delivery_charge = base_delivery * surge_multiplier

    # Free delivery checks
    if (customer_type == "platinum" and order_amount >= 199) or (customer_type == "gold" and order_amount >= 399):
        delivery_charge = 0.0

    # ==========================================
    # 6. DISCOUNT COMPUTATION
    # ==========================================
    discount_pct = 0.0

    # Tier-based membership discount
    if customer_type == "platinum":
        discount_pct = 0.20
    elif customer_type == "gold":
        discount_pct = 0.10
    else:
        if order_amount >= 500:
            discount_pct = 0.05

    # Additional payment/loyalty incentives
    if payment_method == "online" and order_amount >= 400:
        discount_pct += 0.05

    # Capped maximum discount at 30% or Rs 250
    discount_amount = order_amount * discount_pct
    if discount_amount > 250.0:
        discount_amount = 250.0

    # ==========================================
    # 7. PRIORITY STATUS
    # ==========================================
    if customer_type == "platinum" or (customer_type == "gold" and is_peak_hour):
        priority_delivery = "Priority Dispatch"
    elif order_amount >= 1200:
        priority_delivery = "High Value Priority"
    else:
        priority_delivery = "Standard Dispatch"

    # ==========================================
    # 8. FINAL ORDER CATEGORY
    # ==========================================
    if order_amount >= 2000:
        order_category = "Bulk / Feast"
    elif order_amount >= 600:
        order_category = "Family Meal"
    elif order_amount >= 250:
        order_category = "Standard Meal"
    else:
        order_category = "Quick Snack / Solo"

    # ==========================================
    # 9. FINAL PAYABLE AMOUNT
    # ==========================================
    if order_status == "Rejected":
        final_payable = 0.0
    else:
        final_payable = (order_amount - discount_amount) + delivery_charge

    # ==========================================
    # 10. GENERATE ORDER REPORT
    # ==========================================
    print("\n" + "="*45)
    print("         AUTOMATED ORDER REPORT")
    print("="*45)
    print(f"Order Status            : {order_status}")
    if order_status == "Rejected":
        print(f"Rejection Reason        : {rejection_reason}")
    print(f"Manual Review Status    : {'Flagged for Agent' if manual_review else 'Not Required'}")
    print(f"Order Category          : {order_category}")
    print(f"Priority Delivery       : {priority_delivery}")
    print(f"Restaurant Operational  : {restaurant_status}")
    print(f"Cancellation Risk       : {cancellation_risk}")
    print("-" * 45)
    print(f"Base Item Total         : INR {order_amount:.2f}")
    print(f"Discount Applied        : - INR {discount_amount:.2f}")
    print(f"Delivery Charge         : + INR {delivery_charge:.2f}")
    print("-" * 45)
    print(f"FINAL PAYABLE AMOUNT    : INR {final_payable:.2f}")
    print("="*45)

# Run the program
if __name__ == "__main__":
    evaluate_order()