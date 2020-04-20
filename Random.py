from random import choice


class RandomMoviesWithBf:
    def __init__(self):
        self.movie_list = ["I Want to eat your Pancreas","The Garden of Woods","5 Centimeter per Second", "The Secret "
                                                                                                          "World of "
                                                                                                          "Arrietty",
                           "Weathering with you",]
        # self.__chosen_movies = list()
a
    def get_movie_list(self):
        movie_list = choice(self.movie_list)
        return movie_list

    # def get_chosen_movies(self):
    #     pass



m = RandomMoviesWithBf()
print(m.get_movie_list())