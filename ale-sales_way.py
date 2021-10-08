#!/usr/bin/python3
"""
Asymmetric Lightweight Encryption-Symmetric Asymmetric Lightweight Encryption System Without Asymmetric Yet
derivative X -> lim f(x) = (f(x) - f(x1))/(x - x1)
integral Y -> |f(y) dy = F(y) + C -> we need this one because C could one pre known value which means
that the integrated function cannot return a useful value without it. Meaning that f(x) being x = the ascii value
of the encrypted payload, so if we have a function like (1 + 1/x)**x we integrated as:
(y)**x substitution method
y = 1 + 1/x
x = y - 1 = 1/x; x(y-1) = 1; x = 1/(y-1);
dx = dy; dy = 1/(x**2); dy = 1/(1/(y-1))**2
| y**(1/(y-1)) dx
euler e -> lim (1 + 1/n)**n

if we take x and evaluate it in f(x) being f(x) equal to x**2 being x = 3, we get f(3) = 9
if we evaluate it in df(x)/dx x**2 = 2x and that means that the output will be going instead 6, now
the hacker will only now the derived value of the function that has not relevance and they cannot integrate the
function into the original value so because 2x integrated is going to be equal to x**2 + C being C a non know value
a hacker could try with all possibilities from -infinity to +infinity, which could take his entire life to know
at least one byte of the whole payload...  So the destiny peer receive a number that is useless really, it is just
the area under the curve created by the integrate of a function, this function it can be pre known by peers
in the application layer... So there is not transmission for the function (You must understand that the function
it is an algorithm, so must be programmed in the two places)... So once 6 transmitted we know that that 6 is
the result of the derivative of the original function....
Private Key: The original function... for example: (1 + 1/n)**n; x**2
Public Key: 2x one value as "e" = 101 = f(x) = 2*101 = 202 = F(x) = x**2 = 101 X
Public Key: x**2 one value as "e" = 101*101 + C = f(x) = 2

Well in the previous section we cannot figure it out how to use integral with encryption system...
Now, we are going to think about |f(x) = F(x) + C  so if we give it to one function like
1/n we can say that |f(x) = n**-1 = ln(n) so imagine that user is going to use
ln(n) as the public key each value is going to be passed for it and so we can get the tangent to curve relative
to the point n, y where y is going to be determinate by the result of the function and n or x is going to be
the input...
x**2 and i give you 2x so you give me 2 * 3 = 6 and i say x ** 2 = 9

If we have one function imagine x**2 and we tell the other peer that he must use 2x as the public encryption key
he gave us for example for an entry of 3 the result of 6 we use that number in the next equality 2x = 6, so
x = 6/2 and x = 3, so the origin called Adam will decrypt the message using x**2

if we take one function being that function x**2 and we integrated and use it as the private key
for example ((x**3)/3) +C
And we derivate x**2 as 2x and deliver that as the public key...
"""
import random
from datetime import datetime
__author__ = "Esteban Chacon Martin"
__doc__ = "AES XOR or Advanced Encryption System for XOR encryption it is intended to be a lightweight encryption" \
          "system for encrypt faster than using other encryption tools... The firsts versions will be developed" \
          "for testing purposes and maybe they arent secure yet, the versions over the 1.0.0 will be ready for " \
          "productions environments..." \
          "The mathematics behind this are:\n" \
          ""


class AESXor:
    """
    Advanced encryption system with XOR...
    """
    __key: bytes
    __value: bytes
    __timeout: int
    __key_len = 64
    __seed: int
    __steps: int

    def __init__(self, key: bytes = None, timeout=10, key_len=64, seed=2, step=1):
        self.__steps = step
        self.__timeout = timeout
        self.__seed = seed
        if key is None:
            self.__key_len = key_len
            self.generate_key(seed)
        else:
            self.__key_len = len(key)
            self.__key = key

    def generate_key(self, seed, length: int = None):
        """Generate a pretty random pseudo-random key,I tried to make it the most random as possible,
        just imagine this function using two factors the first one consider it as distance factor, which is
        a factor who alter itself at the same time that payload progress, and the second is time factor, which
        means that payload will alter itself no matter how many payload had been sent but instead counting the
        time pasted since the last change or the begin of the creation..."""
        if length is not None:
            self.__key_len = length
        seed %= 25
        self.__steps %= (seed * 4) + 1
        distance_factor = seed + self.__steps
        time_factor = int(datetime.now().timestamp()//self.__timeout)
        time_factor = (time_factor - int(time_factor/10) * 10) + 1
        fibonacci_factor = (self.fibonacci(seed) + 1) % 255
        self.__seed += fibonacci_factor
        self.__key = b""
        for i in range(self.__key_len):
            self.__key += str((((time_factor * fibonacci_factor)+1) /
                               ((distance_factor * fibonacci_factor) + 1))
                              % 256).encode()

    def fibonacci(self, a, b=0, c=1):
        """
        Fibonacci number
        """
        if a > 1:
            return self.fibonacci(a-1, b + c, b)
        return b

    def encrypt(self, payload: bytes):
        self.generate_key(self.__seed)
        res = b""
        for index in range(len(payload)):
            res += chr(payload[index] ^ self.__key[index % self.__key_len]).encode()
        #print(len(self.padding(res)))
        #self.obfuscate(res[0], self.__seed, self.__steps)
        self.__value = self.padding(res)
        return self

    def decrypt(self, payload=None):
        self.generate_key(self.__seed)
        res = b""
        for index in range(len(payload)):
            res += chr(payload[index] ^ self.__key[index % self.__key_len]).encode()
        self.__value = self.padding(res)
        return self

    def integral(self, fnc: bytes):
        response = ""
        return response + "C"

    def derivate(self, fnc: bytes):
        response = ""
        remainder = fnc.strip()
        while (len(remainder) > 0):
            remainder.replace(
                remainder.find(b"(.*)")
            )
        return response

    def get_public_key(self):
        return b"f(x) = 1 / n"

    def get_private_key(self):
        return b"f(x) = ln(x)"

    def compress(self, payload: bytes):
        res = b""
        for i in payload:
            pass
            #res +=  pass

    def padding(self, payload: bytes):
        """
        Fills the output payload with N bytes for obfuscate the output... This makes the result to be greater..
        """
        res = payload
        len_pl = len(payload)
        for i in range(0, len_pl):
            if 2**i > len_pl:
                for x in range(len(payload), (2**i) + 1):
                    res += chr(random.randint(0, 127)).encode()
                break
        return res

    def get_value(self):
        return self.__value

    def __bytes__(self):
        return self.__value

    def __str__(self):
        return self.__value.decode()


if __name__ == "__main__":
    # time.clock_gettime()
    aesXorLock = AESXor(timeout=5, seed=257)
    aesXorUnlock = AESXor(timeout=5, seed=257)
    for i in range(3):
        locked = aesXorLock.encrypt(b"Hola mundo ")
        print(locked.get_public_key())
        #print(locked)
        unlocked = aesXorUnlock.decrypt(locked.get_value())
        print(locked.get_private_key())
        #print(unlocked)
