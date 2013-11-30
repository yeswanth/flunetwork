package infetionspread.internal;

import infetionspread.GraphStatistics;
import infetionspread.Network;
import infetionspread.Node;

import java.util.*;

/**
 * Created with IntelliJ IDEA.
 * User: akash
 * Date: 10/27/13
 * Time: 10:34 PM
 * To change this template use File | Settings | File Templates.
 */
public class DSNSimulation {

    private Network network;

    private final int runtime = 365;

    private void initializeSimulation() {
        network = new Network();
        network.setInfected();
        network.setVaccinated();
    }

    private void runSimulation() {
        GraphStatistics graphStatistics = new GraphStatistics();
        for(int timeInstant = 0; timeInstant < runtime; timeInstant++) {
            graphStatistics.resetStatistics();
            graphStatistics.setTimeInstant(timeInstant);
            network.runSimulationForTimeInstant(graphStatistics);
            graphStatistics.displayStatistics();
        }
    }

    public static void main(String[] args) {
        DSNSimulation dsnSimulation = new DSNSimulation();
        dsnSimulation.initializeSimulation();
        dsnSimulation.runSimulation();
    }
}
