import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

/**
 * Thomas 2, 5
 * Bold the currently selected item in the move list.
 * When someone wins, highlight the three squares that caused the win.
 * 
 * Steven 1, 3
 * Display the location for each move in the format (col, row) in the move history list.
 * Rewrite Board to use two loops to make the squares instead of hardcoding them.
 * 
 * Alyssa 6
 * When no one wins, display a message about the result being a draw.
 *
 * Saron 4
 * Add a toggle button that lets you sort the moves in either ascending or descending order.
**/

let buttonText = "Change to Des"; //SARON CHANGED THIS

  function Square(props){ //THOMAS CHANGED STUFF HERE
    console.log("oof: " + props.winLine)
    return(
      <button className='square' onClick={props.onClick}
      style={props.winLine?{"backgroundColor":"#60CC60"}:{}}>
        {props.value}
      </button>
    )
  }

  class Board extends React.Component {

    renderSquare(i, j) { //STEVEN CHANGED STUFF
      let index = (i*3+j)
      console.log("stuff: " + index)
      return (
        <Square
          value={this.props.squares[i*3+j]}
          onClick={() => this.props.onClick(i, j)}
          winLine={this.props.winLine.find(a=>a===index)>=0} //THOMAS CHANGED STUFF HERE
        />
      );
    }
  
    render() { //STEVEN CHANGED LIKE ALL THE STUFF
      return (
        <div>
          {
            [0,1,2].map((elem, i) => {
              return (
              <div className="board-row">
              {
                [0,1,2].map((elem2, j) => {
                  return(this.renderSquare(i, j))
                })
              }
              </div> )
            })
          }
        </div>
      );
    }
  }
  
  class Game extends React.Component {
    constructor(props){
      super(props)
      this.state = {
        history:[
          {
          squares: Array(9).fill(null),
          }
        ],
        stepNumber: 0,
        xIsNext: true,
      };
    }

    handleClick(i, j){
      let index = (i*3+j) //STEVEN CHANGED STUFF
      const history = this.state.history.slice(0, this.state.stepNumber + 1);
      const current = history[history.length - 1];
      const squares = current.squares.slice();
      if (calculateWinner(squares) || squares[index]){ //STEVEN CHANGED STUFF
        return;
      }
      squares[index] = this.state.xIsNext ? 'X' : 'O';
      this.setState({
        history: history.concat([
          {
          squares: squares,
          coords: "("+i+","+j+")", //STEVEN CHANGED STUFF
          }
        ]),
        stepNumber: history.length,
        xIsNext: !this.state.xIsNext,
      });
    }

    jumpTo(step){
      this.setState({
        stepNumber: step,
        xIsNext: (step % 2) === 0,
      })
    }

    render() {
      const history = this.state.history;
      const current = history[this.state.stepNumber];
      const winner = calculateWinner(current.squares);

      const moves = history.map((obj, move) => { //STEVEN CHANGED STUFF
        console.log("history length" + history.length + " move moves" + move);
        const desc = move ?
          'Go to move #' + move + " " + obj.coords:
          "Go to game start";
        console.log("move" + move);

        return ( //THOMAS CHANGED STUFF HERE
          <li id={move}>
            <button style={this.state.stepNumber===move?{"fontWeight": "bold"}:{}} value="False" onClick={() => this.jumpTo(move)}>{desc}</button>
          </li>
        )
      });

      const moveDec = history.map((obj, moveDec) => { //SARON CHANGED STUFF HERE

        moveDec -= history.length - 1;
        moveDec = Math.abs(moveDec);
  
        const desc2 = moveDec ? 
        "Go to move #" + moveDec  + " " + history[moveDec].coords:
         "Go to game start";
        console.log("move2 " + moveDec);
  
        return (
          <li id={moveDec}>
            <button style={this.state.stepNumber===moveDec?{"fontWeight": "bold"}:{}} value="False" onClick={() => this.jumpTo(moveDec)}>{desc2}</button>
          </li>
        );
      });
  

      let status;
      console.log(winner)
      if (winner && winner === "Tie"){ //ALYSSA CHANGED STUFF HERE
        status = "This has been a draw";
      }
      else if (winner){ //THOMAS CHANGED STUFF HERE
        status = "Winner: " + winner.winner;
      }
      else{
        status = "Next player: " + (this.state.xIsNext ? "X" : "O");
      }

      return ( //SARON CHANGED STUFF HERE
        <div className="game">
          <div className="game-board">
            <div>{status}</div>
            <br/>
            <Board 
              squares={current.squares}
              onClick={(i, j) => this.handleClick(i, j)} //STEVEN CHANGED STUFF
              winLine={winner!=null?winner!=="Tie"?winner.lineWon:[]:[]} //THOMAS CHANGED STUFF HERE
            />
          </div>
          <div className="game-info"> 
            <div>
              <button className="button" onClick={(i) => descOrder(i)}>
                {buttonText}
              </button>
              <ol style={{"display":"block"}} id="asc">{moves}</ol>
              <ol style={{"display":"none"}} reversed id="des">{moveDec}</ol>
            </div>
          </div>
        </div>
      );
    }
  }
  
  function descOrder() { //SARON CHANGED STUFF HERE
    let ascOrder = document.querySelector("#asc");
    let desOrder = document.querySelector("#des");
    let buttonText = document.querySelector(".button");
  
    if (ascOrder.style.display === "block") {
      ascOrder.style.display = "none";
      desOrder.style.display = "block";
      buttonText.innerHTML = "Change to Asc";
    } else {
      desOrder.style.display = "none";
      ascOrder.style.display = "block";
      buttonText.innerHTML = "Change to Des";
    }
    console.log("How u doin");
  }
  

  function calculateWinner(squares){
    const lines =[
      [0,1,2],
      [3,4,5],
      [6,7,8],
      [0,3,6],
      [1,4,7],
      [2,5,8],
      [0,4,8],
      [2,4,6]
    ]
    for(let i = 0; i < lines.length; i++){
      const [a,b,c] = lines[i]
      if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]){
        return {winner:squares[a],lineWon:lines[i]}; //THOMAS CHANGED STUFF HERE
      }
      else if (!squares.includes(null)){ //ALYSSA CHANGED STUFF HERE
        return "Tie";
      }
    }
    return null;
  }

  // ========================================
  
  const root = ReactDOM.createRoot(document.getElementById("root"));
  root.render(<Game />);
  