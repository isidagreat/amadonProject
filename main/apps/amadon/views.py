from django.shortcuts import render, redirect, HttpResponse

def index(request):
	return render(request, "index.html")

def success(request):
	return render(request, "success.html")

def process(request):
	if 'lifetime' not in request.session:
		request.session['lifetime'] = 0
	if 'lifetime_items' not in request.session:
		request.session['lifetime_items'] = 0
	amount = int(request.POST['amount'])
	product = request.POST['product_id']
	if product == '1096' or product == '1097':
		total = 19.99 * amount
		request.session["this_order"] = total
		request.session['lifetime'] += total
		request.session['lifetime_items'] += amount
	elif product == '1098':
		total = 4.99 * amount
		request.session["this_order"] = total
		request.session['lifetime'] += total
		request.session['lifetime_items'] += amount
	elif product == '1090':
		total = 49.99 * amount
		request.session["this_order"] = total
		request.session['lifetime'] += total
		request.session['lifetime_items'] += amount
	return redirect(success)



