package infetionspread;

import java.util.HashSet;
import java.util.Random;
import java.util.Set;

/**
 * Created with IntelliJ IDEA.
 * User: akash
 * Date: 10/27/13
 * Time: 10:20 PM
 * To change this template use File | Settings | File Templates.
 */
public class Node {
    private double susceptibility;
    private double targetSusceptibility;
    private double currentSusceptibility;
    private boolean infected;
    private boolean vaccineEffectCompleted;
    private int infectionTime;
    private Set<Integer> neighbours;

    private Random random;

    private final double vaccineEffectiveness = 0.7;
    private final double infectionImmunity = 0.02;
    private final double susceptibilityRecoveryValue = 0.003;
    private final int recoveryTime = 5;
    private final int vaccineEffectPeriod = 14;

    public double getSusceptibility() {
        return susceptibility;
    }

    public void setSusceptibility(double susceptibility) {
        this.susceptibility = susceptibility;
    }

    public double getTargetSusceptibility() {
        return targetSusceptibility;
    }

    public void setTargetSusceptibility(double targetSusceptibility) {
        this.targetSusceptibility = targetSusceptibility;
    }

    public double getCurrentSusceptibility() {
        return currentSusceptibility;
    }

    public void setCurrentSusceptibility(double currentSusceptibility) {
        this.currentSusceptibility = currentSusceptibility;
    }

    public boolean isInfected() {
        return infected;
    }

    public void setInfected(boolean infected) {
        this.infected = infected;
    }

    public boolean isVaccineEffectCompleted() {
        return vaccineEffectCompleted;
    }

    public void setVaccineEffectCompleted(boolean vaccineEffectCompleted) {
        this.vaccineEffectCompleted = vaccineEffectCompleted;
    }

    public int getInfectionTime() {
        return infectionTime;
    }

    public void setInfectionTime(int infectionTime) {
        this.infectionTime = infectionTime;
    }

    public Set<Integer> getNeighbours() {
        return neighbours;
    }

    public void setNeighbours(Set<Integer> neighbours) {
        this.neighbours = neighbours;
    }

    public Node() {
        random = new Random();
        susceptibility = (double) (random.nextInt(35) / 1000.00) + 0.016;
        currentSusceptibility = targetSusceptibility = susceptibility;
        infected = false;
        vaccineEffectCompleted = true;
        infectionTime = 0;
        neighbours = new HashSet<Integer>();
        System.out.println("Value of susceptibility for node = " + susceptibility);
    }

    public void vaccinate() {
        vaccineEffectCompleted = false;
        targetSusceptibility = susceptibility * (1.0 - vaccineEffectiveness);
    }

    public boolean updateSusceptibility() {
        if(!vaccineEffectCompleted) {
            if(currentSusceptibility > targetSusceptibility) {
                currentSusceptibility -= ((susceptibility * vaccineEffectiveness)/ ((double)vaccineEffectPeriod));
                return true;
            }
            vaccineEffectCompleted = true;
            targetSusceptibility = susceptibility;
        }
        if (currentSusceptibility < targetSusceptibility) {
            currentSusceptibility += susceptibilityRecoveryValue;
            if(currentSusceptibility > targetSusceptibility) {
                currentSusceptibility = targetSusceptibility;
            }
            return true;
        }
        return false;
    }

    public boolean infect(double globalDecayValue) {
        if(isInfected()) return false;
        if (((double) random.nextInt(1001) / 1000.00) < getCurrentSusceptibility()) {
            setInfected(true);
            setInfectionTime(0);
            return true;
        }
        return false;
    }

    public boolean isRecovered() {
        if(!isInfected()) return false;
        infectionTime++;
        if (infectionTime < recoveryTime) {
            return false;
        }
        setInfected(false);
        resetInfection();
        return  true;
    }

    public void resetInfection() {
        infectionTime = 0;
        currentSusceptibility = currentSusceptibility * (1.0 - infectionImmunity);
        targetSusceptibility = susceptibility;
        vaccineEffectCompleted = true;
    }
}