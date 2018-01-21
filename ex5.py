my_name = "Meg R."
my_age = 28 # not a lie
my_height = 63 # inches
my_weight = 128 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Blonde'

in2cm = 2.54
lb2kg = 0.453592

my_heightCm = my_height * in2cm
my_weightKg = my_weight * lb2kg

print "Let's talk about %s." % my_name
print "She's %d inches tall." % my_height
print "She's %.2f cm tall." % my_heightCm
print "She's %d pounds heavy." % my_weight
print "She's %.2f kg heavy." % my_weightKg
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair." %(my_eyes, my_hair)
print "Her teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d, I get %d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight)