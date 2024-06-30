def do_create(self, line):
        """Usage: create <class> <key 1>=<value 2> <key 2>=<value 2> ...
        Create a new class instance with given keys/values and print its id.
        """
        try:
            if not line:
                raise SyntaxError()
            joylist= line.split(" ")

            kwargs = {}
            for j in range(1, len(joylist)):
                key, value = tuple(joylist[j].split("="))
                if value[0] == '"':
                    value = value.strip('"').replace("_", " ")
                else:
                    try:
                        value = eval(value)
                    except (SyntaxError, NameError):
                        continue
                kwargs[key] = value

            if kwargs == {}:
                obj_list = eval(joylist[0])()
            else:
                obj_list= eval(joylist[0])(**kwargs)
                storage.new(obj_list)
            print(obj_list.id)
            obj_list.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
