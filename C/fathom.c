#include <stdio.h>

main()
{
        int     inches, feet, fathoms = 7;

        feet = 6 * fathoms;
        inches = 12 * feet;
        printf("Wreck of the Hesperus\n");
        printf("Its depth at sea in different units:\n");
        printf("        %d fathoms\n", fathoms);
        printf("        %d feet\n", feet);
        printf("        %d inches\n", inches);

}