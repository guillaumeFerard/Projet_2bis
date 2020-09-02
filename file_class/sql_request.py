# coding : utf-8


import sqlite3


class SQL_request:

    def __init__(self, crypto = False):
        self.crypto = crypto
        self.email = False
        self.password = False
        self.connection = sqlite3.connect("SQLite.db")
        self.cursor = self.connection.cursor()


    def get_user_id(self, user):
        # ! fonction qui recupere l'id de l'user
        user = (user,)
        
        self.connection = sqlite3.connect("SQLite.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute('SELECT ID FROM gmh_user WHERE email = ?', user)
        result_email = self.cursor.fetchone()
        return result_email[0]


    def check_email(self, email):
        # ? fonction to check if pseudo is in DB """
        email = (email,)
        # ? create connection to DB
        self.connection = sqlite3.connect("SQLite.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute('SELECT * FROM gmh_user WHERE email = ?', email)
        result_email = self.cursor.fetchone()
        if result_email is None:
            self.email = False
        else:
            self.email = True
        self.connection.close()
        return self.email


    def check_password(self, password):
        # ? fonction to check if password is in DB """
        
        password = (self.to_crypt(password),)

        # ? create connection to DB
        self.connection = sqlite3.connect("SQLite.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute('SELECT * FROM gmh_user WHERE password = ?', password)
        result_pwd = self.cursor.fetchone()
        
        if result_pwd is None:
            self.password = False
        else:
            self.password = True
        
        self.connection.close()
        return self.password


    def get_player_data(self, user):
        user = (user,)
        self.connection = sqlite3.connect("SQLite.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM gmh_player INNER JOIN gmh_map ON gmh_player.id_map = gmh_map.ID WHERE id_user = ?", user)
        # ! recupere data player pour les mettre dans les variables 
        result = self.cursor.fetchall()
        return result


    # ? methode update
    def save_player_pos(self, player, posY, posX):
        new_data = (posX, posY, player)
        # ? create connection to DB
        self.connection = sqlite3.connect("SQLite.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute('UPDATE gmh_player SET pos_X = ?, pos_Y = ? WHERE name = ?', new_data)
        self.connection.commit()
        self.connection.close()


    # ! je créer la méthode qui vas crypter les mdp
    def to_crypt(self, to_crypt):
        # ! créer un dictionnaire par lettre
        self.alphabet_nb = {"a" : 0, 
                             "b" : 1, 
                             "c" : 2,
                             "d" : 3,
                             "e" : 4,
                             "f" : 5,
                             "g" : 6,
                             "h" : 7,
                             "i" : 8,
                             "j" : 9,
                             "k" : 10,
                             "l" : 11,
                             "m" : 12,
                             "n" : 13,
                             "o" : 14,
                             "p" : 15,
                             "q" : 16,
                             "r" : 17,
                             "s" : 18,
                             "t" : 19,
                             "u" : 20,
                             "v" : 21,
                             "w" : 22,
                             "x" : 23,
                             "y" : 24,
                             "z" : 25 }
        self.alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                              'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 
                              'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 
                              't', 'u', 'v', 'w', 'x', 'y', 'z']

        # ! je créer la cle de codage, par rapport a la longeur du mdp
        key_cesar = len(to_crypt)
        list_to_crypt = list(to_crypt)
        result = ""
        
        # ! pour chaque lettre, je vais lui ajouter la clé et mettre dans result notre nouvelle valeur
        for letter in list_to_crypt:
            index_tmp = self.alphabet_nb[letter]
            index_tmp += key_cesar
            result = f"{result}{self.alphabet_list[index_tmp]}"
        
        return result


    def get_class_choice(self, user):
        # ! fonction qui recupere les chemin des deux classe du joueur
        user = (user,)
        class_img = []
        class_name = []
        self.connection = sqlite3.connect("SQLite.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute('SELECT id_class FROM gmh_player WHERE id_user = ?', user)
        result = self.cursor.fetchall()
        for id_class in result:
            self.cursor.execute('SELECT class, img FROM gmh_class WHERE ID = ?', id_class)
            result_class = self.cursor.fetchone()
            class_img.append(result_class[1])
            class_name.append(result_class[0])
        return class_img, class_name

    def get_info_player(self, pseudo, info):
        requete = (pseudo,)
        self.connection = sqlite3.connect("SQLite.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute('SELECT ' + info + ' FROM gmh_player WHERE pseudo = ?', requete)
        result = self.cursor.fetchone()
        return result[0]