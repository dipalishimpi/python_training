1.**None**  
  -  None is used to define a **null value or Null object** in Python. It is not the same as an empty string, a False, or a zero. **It is a data type of the class NoneType object**.    

 - **Null** – There is no null in Python, we can use None instead of using null values.

2.**Numbers** 
   - Numeric objects are immutable.
2.1 **integral**
     - These represent elements from the mathematical set of integers (positive and negative).
     - There are two types of integers:
     2.1.1 **Integer**
        - Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

        2.1.2 **Booleans**
         - These represent the truth values False and True.
         - false=0 and true=1 consider value
         - The two objects representing the values False and    True are the only Boolean objects.
        - when converted to a string, the strings "False" 
        "True" are returned, respectively.
        
     2.2 **Float**
      - Float, or "floating point number" is a number, positive or negative, containing one or more decimals. 

     2.3 **Complex**
       - A complex number has two parts, real part and imaginary part. Complex numbers are represented as A+Bi or A+Bj, where A is real part and B is imaginary part.
       - example  
        >real = 3
         imaginary = 5
         z = complex(real, imaginary)
         print("The complex number is ", z)
         <br>
         output:
         The complex number is  (3+5j)
         
3. **Sequences**
    - These represent finite ordered sets indexed by  non-negative numbers.
     The built-in function len() returns the number of items of a sequence.

    3.1 **Immutable Sequences**
      - An object of an immutable sequence type cannot change once it is created.
      3.1.1 **String**
        - Strings are a group of characters written inside a single or double-quotes. Python does not have a character type so a single character inside quotes is also considered as a string.
        <br>
        - Strings are immutable in nature so we can reassign a variable to a new string but we can’t make any changes in the string.
        example
        >city= ‘China’
         print(city[2])
         city[2] = ‘a’
         Output:
         <br>
         Traceback (most recent call last):
         File “<stdin>”, line 3, in <module>
         TypeError: ‘str’ object does not support item assignment
    
        3.1.2 **Tuple**
          - Tuples are also a sequence of Python objects. A tuple is created by separating items with a comma.  
          - They can be optionally put inside the parenthesis () but it is necessary to put parenthesis in an empty tuple.
          <br>
          
        3.1.3 **Bytes**
          - The bytes() function returns a bytes object.

          - It can convert objects into bytes objects, or create empty bytes object of the specified size.

          - The difference between bytes() and bytearray() is that bytes() returns an object that cannot be modified,  
          and bytearray() returns an object that can be modified.
     
    3.2 **Mutable Sequence**
      - Mutable sequences can be changed after they are created.
      3.2.1 **List**
        - List is also a collection of other python objects but mutable unlike tuple.
        -  Lists are formed by placing a comma-separated list of expressions in square brackets.
      
        3.2.2 **ByteArray**
         - The bytearray() function returns a bytearray object.
         - It can convert objects into bytearray objects, or create empty bytearray object of the specified size.
         - bytearray() returns an object that can be modified.
4. **Set Types** 
    - The sets are basically an unordered . We can use the set for some mathematical operations like set union, intersection, difference etc. 
    - We can also use set to remove duplicates from a collection.
    - The set do not record the element position. - It does not support the indexing, slicing or other sequence related operations.
    
    4.1 **Set**
     - Sets are used to store multiple items in a single variable.
     - Sets are written with curly brackets.
     - Set items are unordered, unchangeable, and do not allow duplicate values.
     - The values **True and 1** are considered the same value in sets, and are treated as duplicates

    4.2 **Frozen set**
     - These represent an immutable set.
     - They are created by the built-in frozenset() constructor.
     - we can't performed add(), remove() kind of opertaion in frozen set.

5. **Mapping**
 5.1 **Dictionary**
    - These represent finite sets of objects indexed by nearly arbitrary values.
    - The key in a dictionary can not be mutable, the reason being that the efficient implementation of dictionaries requires a key’s hash value to remain constant.
    - dictionary is mutable.
    <br>
    - What is a hashable object?
     -An object is hashable if it has a hash value which never changes during its lifetime (it needs a hash() method), and can be compared to other objects (it needs an eq() method). Hashable objects which compare equal must have the same hash value.
     -  All **immutable** built-in objects in Python are hashable like **tuples** while the **mutable** containers like **lists** and **dictionaries** are not hashable. 
     <br>
     
     how does hashmap works?
     how dictionary works?
      https://youtu.be/ea8BRGxGmlA?si=xp6g61FlZG5vYoCl




