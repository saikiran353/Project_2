d_main= {"items":[{"id":1,"name":"Chocolate Milk","type":"base", "price":
100, "available_quantity": 5},
				{"id":2,"name":"Kesar Milk","type":"base", "price": 120, "available_quantity":10},
				{"id":3,"name":"Faluda Milk","type":"base", "price": 110,
"available_quantity": 6},
				{"id":4,"name":"Icecream Scoop","type":"addon", "price": 50, "available_quantity":9},
				{"id":5,"name":"Rose Petals","type":"addon", "price": 25,
"available_quantity": 8},
				{"id":6,"name":"Chocolate chips","type":"addon", "price": 20, "available_quantity":2},
				{"id":7,"name":"Oreo Biscuit","type":"addon", "price": 30,
"available_quantity": 5}]}

######## needs ########
d=d_main.copy()
Total_order_summary={ }
Total_orders=[ ]
#######---------------#######		
# shows the detailes of item
def list_summary():
	for i in d['items']:
		for k ,v in i.items():
			print(k +':' +str(v))
		print()

# calculates and shows the total revenue
def total_order_summary():
		print(Total_order_summary)
		total_price=0
		print('- '*21)
		print('{:24s} | {:3s} | {:20s}'.format('item', 'qty', 'price-$'))
		print('- '*21)
		for key, values in Total_order_summary.items():
			if key !=None:
				print('{:24s} | {:3d} | {:7d}'.format(key, values[1], values[1]*values[0]))
				total_price+=values[1]*values[0]

		print('- '*21)
		print('Total Revenue Generated= {}'.format(total_price))
		print('- '*21)
		
		
# asks input for orders
def choose_opt():
	try:
		print('1. creat order\n2. view item status\n3. Total orders')
		options=[1,2,3]
		user=int(input('choose the review option(1/2/3): '))
		while True:
			if user not in options:
				print('please choose apprpriate option')
				user=int(input('choose the review option(1/2/3): '))
			else:
				break
		if user==3 or 2 or 1:
			return user
	except ValueError :
		print('please choose only as given')
		choose_opt()
		
# base_item_dict will store the base item pairs
base_item_dict={ }
# shows the base items to select
def show_base_items():
	
	for i in d['items']:
			if i['type']=='base' and i['name'] not in base_item_dict:
				base_item_dict[i['name']]=[i['price'], i["available_quantity"]]
			if  i['type']=='base' :
				#print(base_item_dict[i['name']])
								base_item_dict[i['name']][1]=i["available_quantity"]

				
					
			
	#print(base_item_dict)
	print('- '*19)
	print('{:5s} {:15s} {:5s} {:20s}'.format('s.no', 'items', 'price', 'available'))
	print('- '*19)
	for z,(x,i) in enumerate(base_item_dict.items()):
				#print(z+1, x + '--->$' + str(i[0]) +'----'+ str(i[1]))
				print('{:5s} {:15s} {:5s} {:20s}'.format(str(z+1), x, str(i[0]), str(i[1])))
	print('- '*19)


# base_item_dict will store the base item pairs								
addon_item_dict={ }
# will shows the addon item pairs
def show_addon_items():
	
	for i in d['items']:
			if i['type']=='addon' and i['name'] not in addon_item_dict:
							addon_item_dict[i['name']]=[i['price'], i["available_quantity"]]
	#print(addon_item_dict)
	print('- '*19)
	print('{:5s} {:15s} {:5s} {:20s}'.format('s.no', 'items', 'price', 'available'))
	print('- '*19)
	for z,(x,i) in enumerate(addon_item_dict.items()):
				#print(z+1, x + '--->$' + str(i[0]) +'----'+ str(i[1]))
				print('{:5s} {:15s} {:5s} {:20s}'.format(str(z+1), x, str(i[0]), str(i[1])))
	print(len(addon_item_dict)+1,'done')
	print('- '*19)
			
# responsible to select base item and returns tuple of item & price
def choose_base_item():
	base_item_lst = [key for key, values in base_item_dict.items()]
	try:
		options=[i+1 for i in range(len(base_item_lst))]
		user=int(input('choose any of the above items: '))
		while True:
			if user not in options and user != len(options)+1:
				print('please choose apprpriate option')
				user=int(input('choose any of the above items: '))
			else:
				break
		for i in range(len(options)):	
			if user==options[i]:
				item=base_item_lst[i]
				# price is list of price and qty.
				price=base_item_dict[base_item_lst[i]]
				print(item, price[0])
				return (item, price[0])
		
	except ValueError :
		print('please choose only as given')
		choose_base_item()
						

# responsible to select addon item and returns tuple of item & price
def choose_addon_item():
	addon_item_lst = [key for key, values in addon_item_dict.items()]
	try:
		options=[i+1 for i in range(len(addon_item_lst))]
		user=int(input('choose any of the above items: '))
		while True:
			if user not in options and user != len(options)+1:
				print('please choose apprpriate option')
				user=int(input('choose any of the above items: '))
			else:
				break
		for i in range(len(options)):	
			if user==options[i]:
				item=addon_item_lst[i]
				price=addon_item_dict[addon_item_lst[i]]
				print(item, price[0])
				return (item, price[0])
		else:
			print('is it')
			return None

	except ValueError :
		print('please choose only as given')
		return choose_addon_item()


# returns quantity of items
def quantity(type):
		if type != None:
			try:
				user=int(input('choose the number of quantities you want: '))
				while True:
					if user != int(user):
						print('please choose appropriate number of items: ')
						user=int(input('choose the number of quantities you want: '))
					else:
						break
				return user
			except ValueError :
				print('please choose only numbers(ex:.,1.2.3.4......)')
				return quantity(type)
	

# stores order items temporarily	
order_lst=[ ]
# shows order summary and clears order list to replace next order
# add orders list to Total orders list
def order_summary():
				
				total_price=0
				print('- '*21)
				print('{:24s} | {:3s} | {:20s}'.format('item', 'qty', 'price-$'))
				print('- '*21)
				for i in range(len(order_lst)):
					if order_lst[i][0] !=None:
					
						print('{:24s} | {:3d} | {:7d}'.format(order_lst[i][0][0], order_lst[i][1], (int(order_lst[i][0][1]))*order_lst[i][1]))
						total_price+=int(order_lst[i][0][1])*order_lst[i][1]
						# update quantity in d(main dictionary)
						for j in d['items']:
							if j['name'] == order_lst[i][0][0]:
	 							j["available_quantity"] -= order_lst[i][1]		
					else:
						pass
				print('- '*21)
				print('Total price = {}'.format(total_price))
				print('- '*21)
				
				#---------------------------@
				for ((item, price), availability) in order_lst:
					if item not in Total_order_summary:
						Total_order_summary[item]=[price,availability]
					else:
						Total_order_summary[item][1]+=availability		
				#---------------------------@
			
				Total_orders.append(order_lst.copy())
				order_lst.clear()
					

# checks availability of items		
def check_avail(type):
	
	if type != None:
		type_quantity =quantity(type)
		
		for i in d['items']:
			if i['name'] == type[0] and i["available_quantity"] >=1 and type_quantity <= i["available_quantity"]:
					print('yes avilable')
					order_lst.append((type, type_quantity))
					return
			
			elif i['name'] == type[0] and i["available_quantity"] == 0:
				print('item no longer available. please choose again:')
				return 0
				
			elif i['name'] == type[0] and type_quantity > i["available_quantity"]:
				print(' Sorry, this item is insufficient. please choose less quantity: ')
				return check_avail(type)
		
# gets base item and returns it					
def base_item_review():
			
			show_base_items()
			base_item=choose_base_item()
			return base_item
	
# gets addon item and returns it
def addon_item_review():

							show_addon_items()
							addon_item=choose_addon_item()
						
							return addon_item
					
			
# starts ordering 							
def order():
	option= choose_opt()
	
	if option==2:
		list_summary()
		return 0
	
	elif option==3:
		total_order_summary()
		
	else:
		print('items:')
		print('main item')

		#--------------------------------------------------------#
		
		base_item=base_item_review()
		check=check_avail(base_item)
		if check==0:
			return order()
		for i in range(3):
			addon_item=addon_item_review()
			check_avail(addon_item)
			if check==0:
				break
				order()
		order_summary()
		
		#--------------------------------------------------------#

# responsible for all ordering process repeatedly.
def main():
	start=int(input('press 1 to start:'))
	while True:
		if start==1:
			o=order()
			if o!= 0:
				print('1.confirm\n2.cancel')
				while True:
					try:
						user_confirm=int(input('please choose your order(confirm/cancel): '))
						break
			
					except ValueError:
						print('wrong input. try again')
				if user_confirm==1:
					print(Total_orders)

				else:
					print('order cancelled')
					Total_orders.popitem()
			else:
				return
				
		else:
			break


main()

#show_base_items()
#choose_base_item()
#show_addon_items()
#choose_addon_item()

