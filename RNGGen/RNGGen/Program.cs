using System;
using System.Linq;

namespace RNGGen
{
    class Program
    {
        static void RngShowcase(ushort input)
        {
            ushort s0, s1;
            s0 = (ushort)(input ^ (input << 8));
            Console.WriteLine("Step 1: Have 3 shorts input, s0 and s1. XOR input and input's lower byte.\nResult: s0 = {0:X}\n", s0);

            input = (ushort)((s0 << 8) | (s0 >> 8));//0000xlow and xtop0000
            Console.WriteLine("Step 2: Swap s0's bytes.\nResult: input = {0:X}\n", input);

            s0 = (ushort)(input ^ ((s0 & 0xFF) << 1));//take lower byte lamo, shift 1 bit to the left for the lower byet
            Console.WriteLine("Step 3: Take lower byte of s0, and shift it 1 bit to the left. XOR input and the result.\nResult: s0 = {0:X}\n", s0);

            s1 = (ushort)(0xFF80 ^ (s0 >> 1));
            Console.WriteLine("Step 4: Shift s0's bits to the right once, then XOR s0 and the constant 0xFF80.\nResult: s1 = {0:X}\n", s1);

            if (s0 % 2 == 1)
            {
                input = (ushort)(s1 ^ 0x8180);
            }
            else
            {
                input = (ushort)(s1 ^ 0x1FF4);
            }
            Console.WriteLine("Step 5: If s0 is odd, XOR s1 with 0x8180, else XOR with 0x1FF4.\nResult: input = {0:X}\n", input);
            //thend
        }
        static ushort RngFunction(ref ushort input)//ref cuz need to store the used rng in current_rng
        {
            ushort s0, s1;
            s0 = (ushort)(input ^ (input << 8));
            
            input = (ushort)((s0 << 8) | (s0 >> 8));//0000xlow and xtop0000

            s0 = (ushort)(input ^ ((s0 & 0xFF) << 1));//take lower byte lamo, shift 1 bit to the left for the lower byet

            s0 >>= 1;
            s1 = (ushort)(0xFF80 ^ s0);

            if (s0 % 2 == 1)
            {
                input = (ushort)(s1 ^ 0x8180);
            }
            else
            {
                input = (ushort)(s1 ^ 0x1FF4);
            }

            return input;
        }
        static void Main(string[] args)
        {
            if (args.Contains("m"))//stupid stuff
            {
                Console.WriteLine("I thought learning C++ would sound cool, but it turned out to be terrible for a newbie like me...\nSo I tried c# instead. C# turns out to just be spicy Python. yay i don't want to go to schoolsdlkfjdasj;");
            }
            else
            {
                try
                {
                    ushort try_rng = (ushort)Convert.ToInt32(args[0]);
                    Console.WriteLine("Generated number: {0} => {1}", try_rng, RngFunction(ref try_rng));
                    if (try_rng % 3 == 0) { Console.WriteLine("try to run this program on cmd with '-m' at the back!"); }
                    Console.WriteLine("Press anything to exit...");
                    Console.ReadKey(true);
                    Environment.Exit(0);
                }

                catch (Exception)
                {
                    ;//burh
                }
            }

            Console.WriteLine("================\nThe RNG function\n================");
            Console.WriteLine("The RNG function in SM64 is recreated by me for no reason. Its solution is even in https://www.youtube.com/watch?v=MiuLeTE2MeQ by pannen");
            Console.WriteLine("I just wanted to find some easy things to type in my first C# program\n");

            ushort current_rng = 0xDEAF;
            RngShowcase(current_rng);

            current_rng = 0;
            Console.WriteLine("First 100 RNGs produced by the function shown below:");

            for (int i = 1; i <= 100; ++i) {
                Console.WriteLine("{0}: {1}", i.ToString("000"), RngFunction(ref current_rng).ToString("00000"));
            }

            Console.WriteLine("\nwahooo\n");

            

            Console.WriteLine("Press anything to end the program...(hint, run this program on cmd and add any number within 0 - 65536 to the end of the command)\r");
            Console.ReadKey(true);
        }
    }
}
