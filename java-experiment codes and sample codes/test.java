import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.awt.Color;
import javax.awt.Graphics;

public class Circle extends Jpanel{

	public void paint(Graphics g){
		
		setSize(500,500);
		g.drawOval(100,100,50,50);
		
		g.setColor(color.GREEN);
		
		g.fillOval(100,100,50,50);
		//g.setColor(color.blue);
		
		g.drawRect(30,30,50,10);
	}
	
	public static void main(String [] args){

		JFrame MainFrame = new JFrame();
		MainFrame.setSize(600,600);
		Circle CircleclePanel = new Circle();
		
		MainFrame.add(CirclePanel);
		MainFrame.setVisible(True);
	}
	

}
