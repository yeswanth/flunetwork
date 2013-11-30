package infetionspread;

import java.util.*;

/**
 * Created with IntelliJ IDEA.
 * User: akash
 * Date: 11/29/13
 * Time: 6:35 PM
 * To change this template use File | Settings | File Templates.
 */
public class Network {

    private Map<Integer, Node> graph = new HashMap<Integer, Node>();
    private Set<Integer> varyingSusceptibilityNodes = new HashSet<Integer>();
    private Set<Integer> infectedNodes = new HashSet<Integer>();

    private Random random;

    private final int numberOfNodes = 10000;
    private final int multiplicationFactor = 5;
    private final int adjacentNodes = 15;
    private final int noInfected = 1;
    private final int noVaccinated = 1000;
    private final double globalDecayValue = 0.00000025;

    public Map<Integer, Node> getGraph() {
        return graph;
    }

    public void setGraph(Map<Integer, Node> graph) {
        this.graph = graph;
    }

    public Set<Integer> getVaryingSusceptibilityNodes() {
        return varyingSusceptibilityNodes;
    }

    public void setVaryingSusceptibilityNodes(Set<Integer> varyingSusceptibilityNodes) {
        this.varyingSusceptibilityNodes = varyingSusceptibilityNodes;
    }

    public Set<Integer> getInfectedNodes() {
        return infectedNodes;
    }

    public void setInfectedNodes(Set<Integer> infectedNodes) {
        this.infectedNodes = infectedNodes;
    }

    public Network() {
        random = new Random();
        initializeGraph();
    }

    private void initializeGraph() {
        for (int current_node = 0; current_node < numberOfNodes; current_node++) {
            graph.put(current_node, new Node());
            if(current_node == 0) continue;
            for(int count = 0; count < random.nextInt(current_node); count++) {
                int neighbour = random.nextInt(current_node);
                if(graph.get(current_node).getNeighbours().size() >= adjacentNodes) break;
                if(graph.get(neighbour).getNeighbours().size() >= adjacentNodes) continue;
                graph.get(current_node).getNeighbours().add(neighbour);
                if(graph.get(neighbour).getNeighbours().add(current_node)) {
                    System.out.println("Adding link between " + current_node + " and " + neighbour);
                }
            }
        }
    }

    public void runSimulationForTimeInstant(GraphStatistics graphStatistics) {
        updateSusceptibilities();
        graphStatistics.setNodesInfectedByDispersionEffect(proximityEffect());
        graphStatistics.setNumberOfRecoveredNodes(checkRecoveryState());
        graphStatistics.setNumberOfNewlyInfectedNodes(spreadInfection());
        graphStatistics.setNumberOfInfectedNodes(infectedNodes.size());
    }

    public int getNumberOfInfectedNodes() {
        return infectedNodes.size();
    }

    private void updateSusceptibilities() {
        Set<Integer> loopListVariable = new HashSet<Integer>();
        loopListVariable.addAll(varyingSusceptibilityNodes);
        for(int currentNode : loopListVariable) {
            if(!graph.get(currentNode).updateSusceptibility()) {
                varyingSusceptibilityNodes.remove(currentNode);
            }
        }
    }

    private int checkRecoveryState() {
        int recoveredNodes = 0;
        Set<Integer> loopListVariable = new HashSet<Integer>();
        loopListVariable.addAll(infectedNodes);
        for(int currentNode : loopListVariable) {
            if(graph.get(currentNode).isRecovered()) {
                System.out.println("+++Newly recovered node : " + currentNode);
                recoveredNodes++;
                infectedNodes.remove(currentNode);
                varyingSusceptibilityNodes.add(currentNode);
            }
        }
        return recoveredNodes;
    }

    private int spreadInfection() {
        int newlyInfected = 0;
        Set<Integer> loopListVariable = new HashSet<Integer>();
        loopListVariable.addAll(infectedNodes);
        for(int infectedNode : loopListVariable) {
            for(int currentNode : graph.get(infectedNode).getNeighbours()) {
                if(graph.get(currentNode).infect(globalDecayValue)) {
                    System.out.println("---Newly infected node : " + currentNode);
                    newlyInfected++;
                    infectedNodes.add(currentNode);
                }
            }
        }
        return newlyInfected;
    }

    private int proximityEffect() {
        int nodesInfectedByDispersionEffect = 0;
        double looplimit = (((double) infectedNodes.size() / numberOfNodes) * multiplicationFactor);
        for(int count = 0; count < (int)looplimit; count++) {
            int currentNode = random.nextInt(numberOfNodes);
            if(graph.get(currentNode).forceInfect()) {
                infectedNodes.add(currentNode);
                System.out.println("Node infected by dispersion effect : " + currentNode);
                nodesInfectedByDispersionEffect++;
            }
        }
        return nodesInfectedByDispersionEffect;
    }

    public void setInfected() {
        for(int count = 0; count < noInfected; count++) {
            int infected_node = random.nextInt(graph.size());
            graph.get(infected_node).setInfected(true);
            if(!infectedNodes.add(infected_node)) {
                count--;
                continue;
            }
            graph.get(infected_node).setInfectionTime(0);
            System.out.println("Added infected node : " + infected_node);
        }
    }

    public void setVaccinated() {
        for(int count = 0; count < noVaccinated; count++) {
            int vaccinated_node = random.nextInt(graph.size());
            graph.get(vaccinated_node).vaccinate();
            if(!varyingSusceptibilityNodes.add(vaccinated_node)) {
                count--;
                continue;
            }
            //FIXME if already infected?
            graph.get(vaccinated_node).setInfected(false);
            infectedNodes.remove(vaccinated_node);
            System.out.println("Added vaccinated node : " + vaccinated_node);
        }
    }
}
