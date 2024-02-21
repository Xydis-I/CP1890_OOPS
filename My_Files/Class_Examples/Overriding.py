from My_Files.Class_Exercises.C2_19_2024 import InheritanceProductData as ipd

product1 = ipd.get_products()[0]

print(dir(product1))

print(product1)


from Subclasses import CustomRequestError


def read_movies():
    try:
        movies = []
        with open('movies.csv') as file:
            pass
    except FileNotFoundError:
        raise CustomRequestError('This is my error')
    except Exception:
        raise CustomRequestError('This is generic error')


try:
    movies = read_movies()
except CustomRequestError as e:
    print('CustomRequestError', e)
