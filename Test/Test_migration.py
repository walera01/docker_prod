import pymysql
import psycopg2


def main():
#connect mysql
    try:
        connection = pymysql.connect(
            host = "my_root",
            password = "admin",
            port=3306,
            user="root",
            database="my_bd",
            cursorclass = pymysql.cursors.DictCursor,
        )
        print("successfully connect mysql ")
        # connect postgres
        try:
            connection2 = psycopg2.connect(
                host="my_postgres",
                password="admin",
                port=5432,
                user="postgres",
                database="postgres",
            )
            print("successfully connect postgress ")
            #
            try:
                post_con = connection2.cursor()
                sql_con = connection.cursor()
                sql_con.execute("Show tables;")
                table_sql = sql_con.fetchall()

                # migration tables and rows
                for x in table_sql:
                    print(x)
                    print(x['Tables_in_my_bd'])
                    select = f"SHOW FIELDS FROM {x['Tables_in_my_bd']};"
                    sql_con.execute(select)
                    myresult1 = sql_con.fetchall()

                    create_table = f"CREATE TABLE if not exists {x['Tables_in_my_bd']}("
                    for i in myresult1:
                        create_table += i['Field']+" "+i["Type"]
                        if i != myresult1[-1]:
                            create_table +=","
                    create_table += ")"
                    # print(create_table)
                    post_con.execute(create_table)
                    connection2.commit()
                    connection.commit()


                # migration data users
                copy_data1 = "SELECT * FROM users;"
                copy_1 = sql_con.execute(copy_data1)
                copy1 = sql_con.fetchall()
                migration = f"INSERT INTO users(id,name) VALUES "
                for q in copy1:
                    migration += f"({q['id']},'{q['name']}')"
                    if q != copy1[-1]:
                        migration += ","
                    else:
                        migration += ";"
                print(migration)
                post_con.execute(migration)
                connection2.commit()

                # migration data adresses
                copy_data1 = "SELECT * FROM adresses;"
                copy_1 = sql_con.execute(copy_data1)
                copy1 = sql_con.fetchall()
                migration = f"INSERT INTO adresses(id,name) VALUES "
                for q in copy1:
                    migration += f"({q['id']},'{q['name']}')"
                    if q != copy1[-1]:
                        migration += ","
                    else:
                        migration += ";"
                print(migration)
                post_con.execute(migration)
                connection2.commit()

                # migration data roles
                copy_data1 = "SELECT * FROM roles;"
                copy_1 = sql_con.execute(copy_data1)
                copy1 = sql_con.fetchall()
                migration = f"INSERT INTO roles(id,rol) VALUES "
                for q in copy1:
                    migration += f"({q['id']},'{q['rol']}')"
                    if q != copy1[-1]:
                        migration += ","
                    else:
                        migration += ";"
                print(migration)
                post_con.execute(migration)
                connection2.commit()

            except Exception as e:
                print("Not found anything", e)
            finally:
                connection2.close()

        except:
            print("Error connection postgres")

    except:
        print("Error connection mysql")
    finally:
        connection.close()


if __name__ == "__main__":
    main()