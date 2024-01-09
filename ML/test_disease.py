import numpy as np
from keras.models import load_model

from keras.applications.vgg16 import preprocess_input
from keras.preprocessing.image import ImageDataGenerator

def predict():
    print("Loading model...")
    model = load_model('ml/model.hdf5')

    data_generator = ImageDataGenerator(preprocessing_function=preprocess_input)

    test_generator = data_generator.flow_from_directory(
        directory='media/input',
        target_size=(200, 150),
        batch_size=1,
        class_mode=None,
        shuffle=False,
        seed=123
    )

    test_generator.reset()

    pred = model.predict_generator(test_generator, steps=len(test_generator), verbose=1)
    print("predicted data:",pred)
    predicted_class_indices = np.argmax(pred, axis=1)
    print(predicted_class_indices)
    
    label = [
        'Potato early blight', 'Potato healthy', 'Potato late blight',
        'Rice bacterial leaf blight', 'Rice brown spot', 'Rice leaf smut',
        'Tomato bacterial spot', 'Tomato early blight', 'Tomato late blight'
    ]

    print(label[predicted_class_indices[0]])

    remedies = [
        """ Maintaining optimum growing conditions, including proper fertilization, irrigation, and management of other pests.""",

        """ Crops are good in condition,maintain properly.""",

        """ Eliminating cull piles and volunteer potatoes, using proper harvesting and storage practices, and applying fungicides when necessary.""",

        """ Use balanced amounts of plant nutrients, especially nitrogen,\
        \n Ensure good drainage of fields (in conventionally flooded crops) and nurseries,\
        \n Keep fields clean. Remove weed hosts and plow under rice stubble, straw, rice ratoons and volunteer seedlings, which can serve as hosts of bacteria,\
        \n Allow fallow fields to dry in order to suppress disease agents in the soil and plant residues.""",

        """ Prune and remove heavily affected leaves,\
        \n Provide frequent treatment of neem oil or another fungicide to the foliage,\
        \n Avoid getting water onto the leaves as it recovers,\
        \n Keep the plant away from other plants temporarily,\
        \n Monitor daily to ensure the infection has stopped spreading.""",

        """ Use of disease-free seeds that are selected from healthy crop,\
        \n Seed treatment with carbendazim 2.0g/kg of seeds,\
        \n Control insect pests,\
        \n Split application of nitrogen is recommended,\
        \n Removal and proper disposal of infected plant debris.""",

        """ Remove symptomatic plants from the field or greenhouse to prevent the spread of bacteria to healthy plants,\
        \n Burn, bury or hot compost the affected plants and DO NOT eat symptomatic fruit.""",

        """ Cover the soil under the plants with mulch, such as fabric, straw, plastic mulch, or dried leaves,\
        \n Water at the base of each plant, using drip irrigation, a soaker hose, or careful hand watering, \
        \n Pruning the bottom leaves can also prevent early blight spores from splashing up from the soil onto leaves.""",
        
        """ Spraying fungicides is the most effective way to prevent late blight."""
    ]
    pesticides = ['CHLOROTHALONIL','No need','METALAXYL','STREPTOMYCIN SULPHATE','GRISEPFULVIN',
                  'COPPER OXYCHLORIDE','AZOXYSTROBIN','COPPER HYDROXIDE','PROPINEB']
    print(remedies[predicted_class_indices[0]])
    remedies_text = remedies[predicted_class_indices[0]]
    label_text = label[predicted_class_indices[0]]
    pesticide_text = pesticides[predicted_class_indices[0]]

    return label_text,remedies_text,pesticide_text