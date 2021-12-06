from model import curators
from model import groups
from model import students
from model import subjects
from view import view

v = view()
c = curators()
g = groups()
st = students()
s = subjects()

cont = True
while(cont):
    com = v.readCommand()
    if (com == 'exit'):
        cont = False
    elif (com == 'create' or com == 'delete' or com == 'update'):
        tab = v.readTable()
        if(com == 'delete' and tab == 'curators'):
            id = v.getNum()
            c.delete(id)
        elif(com == 'create' and tab == 'curators'):
            id = v.getNum()
            name = v.getStr()
            surname = v.getStr()
            phone = v.getStr()
            c.create(id, name, surname, phone)
        elif(com == 'update' and tab == 'curators'):
            id = v.getNum()
            name = v.getStr()
            surname = v.getStr()
            phone = v.getStr()
            c.update(id, name, surname, phone)
        elif(com == 'delete' and tab == 'groups'):
            id = v.getNum()
            g.delete(id)
        elif(com == 'create' and tab == 'groups'):
            id = v.getNum()
            code = v.getStr()
            c_id = v.getNum()
            g.create(id, code, c_id)
        elif(com == 'update' and tab == 'groups'):
            id = v.getNum()
            code = v.getStr()
            c_id = v.getNum()
            g.update(id, code, c_id)
        elif(com == 'delete' and tab == 'students'):
            id = v.getNum()
            st.delete(id)
        elif(com == 'create' and tab == 'students'):
            id = v.getNum()
            name = v.getStr()
            surname = v.getStr()
            g_id = v.getNum()
            st.create(id, name, surname, g_id)
        elif(com == 'update' and tab == 'students'):
            id = v.getNum()
            name = v.getStr()
            surname = v.getStr()
            g_id = v.getNum()
            st.update(id, name, surname, g_id)
        elif(com == 'delete' and tab == 'subjects'):
            id = v.getNum()
            s.delete(id)
        elif(com == 'create' and tab == 'subjects'):
            id = v.getNum()
            name = v.getStr()
            c_id = v.getNum()
            s.create(id, name, c_id)
        elif(com == 'update' and tab == 'subjects'):
            id = v.getNum()
            name = v.getStr()
            c_id = v.getNum()
            s.update(id, name, c_id)
        else:
            print('Invalid values')
    else:    
        print('Invalid values')