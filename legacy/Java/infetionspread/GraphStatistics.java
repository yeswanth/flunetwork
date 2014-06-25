package infetionspread;

/**
 * Created with IntelliJ IDEA.
 * User: akash
 * Date: 11/29/13
 * Time: 7:58 PM
 * To change this template use File | Settings | File Templates.
 */
public class GraphStatistics {
    private int timeInstant;
    private int numberOfInfectedNodes;
    private int numberOfNewlyInfectedNodes;
    private int numberOfRecoveredNodes;
    private int nodesInfectedByDispersionEffect;

    public int getTimeInstant() {
        return timeInstant;
    }

    public void setTimeInstant(int timeInstant) {
        this.timeInstant = timeInstant;
    }

    public int getNumberOfInfectedNodes() {
        return numberOfInfectedNodes;
    }

    public void setNumberOfInfectedNodes(int numberOfInfectedNodes) {
        this.numberOfInfectedNodes = numberOfInfectedNodes;
    }

    public int getNumberOfNewlyInfectedNodes() {
        return numberOfNewlyInfectedNodes;
    }

    public void setNumberOfNewlyInfectedNodes(int numberOfNewlyInfectedNodes) {
        this.numberOfNewlyInfectedNodes = numberOfNewlyInfectedNodes;
    }

    public int getNumberOfRecoveredNodes() {
        return numberOfRecoveredNodes;
    }

    public void setNumberOfRecoveredNodes(int numberOfRecoveredNodes) {
        this.numberOfRecoveredNodes = numberOfRecoveredNodes;
    }

    public int getNodesInfectedByDispersionEffect() {
        return nodesInfectedByDispersionEffect;
    }

    public void setNodesInfectedByDispersionEffect(int nodesInfectedByDispersionEffect) {
        this.nodesInfectedByDispersionEffect = nodesInfectedByDispersionEffect;
    }

    public void displayStatistics() {
        System.out.println("---------- STATISTICS FOR TIME INSTANT : " + timeInstant + " ---------");
        System.out.println("Number of infected nodes               : " + numberOfInfectedNodes);
        System.out.println("Number of nodes infected by dispersion : " + nodesInfectedByDispersionEffect);
        System.out.println("Number of newly infected nodes         : " + numberOfNewlyInfectedNodes);
        System.out.println("Number of recovered nodes              : " + numberOfRecoveredNodes);
    }

    public void resetStatistics() {
        timeInstant = 0;
        numberOfInfectedNodes = 0;
        numberOfRecoveredNodes = 0;
    }
}
