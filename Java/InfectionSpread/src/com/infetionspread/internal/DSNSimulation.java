package com.infetionspread.internal;

import com.infetionspread.GraphStatistics;
import com.infetionspread.Network;

/**
 * Created with IntelliJ IDEA.
 * User: akash
 * Date: 10/27/13
 * Time: 10:34 PM
 * To change this template use File | Settings | File Templates.
 */
public class DSNSimulation {

    private int totalInfected;

    private Network network;

    private final int runtime = 365;

    public int getTotalInfected() {
        return totalInfected;
    }

    public void setTotalInfected(int totalInfected) {
        this.totalInfected = totalInfected;
    }

    private void initializeSimulation() {
        network = new Network();
        network.setInfected();
        network.setVaccinated();
        totalInfected = network.getNumberOfInfectedNodes();
    }

    private void runSimulation() {
        GraphStatistics graphStatistics = new GraphStatistics();
        for(int timeInstant = 0; timeInstant < runtime; timeInstant++) {
            graphStatistics.resetStatistics();
            graphStatistics.setTimeInstant(timeInstant);
            network.runSimulationForTimeInstant(graphStatistics);
            graphStatistics.displayStatistics();
            totalInfected += graphStatistics.getNumberOfNewlyInfectedNodes();
        }
    }

    private void endSimulation() {
        System.out.println("------------------------- Ending Simulation -------------------------");
        System.out.println("Total number of nodes infected during simulation : " + totalInfected);
    }

    public static void main(String[] args) {
        DSNSimulation dsnSimulation = new DSNSimulation();
        dsnSimulation.initializeSimulation();
        dsnSimulation.runSimulation();
        dsnSimulation.endSimulation();
    }
}