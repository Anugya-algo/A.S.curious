#DICTIONARIES
car1={'brand':'Audi','model':'GL-43'}#'key':'value'
car2=dict(brand="BMW",model="Q8")
car1['model']='GHL-34'
car2.update({'model':'y4'}) 
car2.update({'color':'red'}) #modificationa and addition using update() in different
print(car2.fromkeys())
print(car1,car2)
print(len(car1))
print(car1['model'],car2['model'])
print(car1.get('brand'))
ck=car1.keys()
cv=car1.values()
ci=car1.items()
print(f"{ci}\n{cv}\n{ck}")#f is formatted string

