class Solution {
    public int[] plusOne(int[] digits) {
        return this.addOne(digits, digits.length - 1);
    }
    
    private int[] moveArray(int[] array) {
        int[] new_array = new int[array.length + 1];
        new_array[0] = 1;
        for (int i = 0; i < array.length; i++) {
            new_array[i + 1] = array[i];
        }
        return new_array;
    }

    private int[] addOne(int[] digits, int index) {
        if (digits[index] < 9) {
            digits[index] += 1;
        } else {
            digits[index] = 0;
            if (index == 0) {
                return this.moveArray(digits);
            }
            return this.addOne(digits, index - 1);
        }
        return digits;
    }
}
