import mph

# The start() function returns a client object,
# i.e. an instance of the Client class.
client = mph.start()

# Creates a new model and returns it as a [`Model`](#Model) instance.
# pymodel is an object of class "Model"
# pymodel = client.create('Model')
# model = client.create('capacitor')
model = client.load('Axisymmetric.mph')

model.component("comp1").geom().create("geom1", 2);
model.component("comp1").geom("geom1").axisymmetric('true');

model.mesh()

print(mph.tree(model))

model.solve('Study 1')

model.export('Image', 'magB.png')
#
model.save('Axisymmetric_modified.mph')

