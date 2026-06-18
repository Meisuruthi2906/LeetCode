class Solution {
    public double angleClock(int hour, int minutes) {

        double minute=minutes*6;
        double hourHand=(hour%12)*30+(minutes*0.5);
        double variaty=Math.abs(hourHand-minute);
        return Math.min(variaty,360.0-variaty);
    }
}

        
    