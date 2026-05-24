import './LigneBus.css';

function LigneBus({ numero, depart, arrivee, arrets, couleur, estSelectionnee, onClick }) {
  return (
    <div
      className={`ligne-bus ${estSelectionnee ? 'ligne-bus-active' : ''}`}
      onClick={onClick}
    >
      <div className="ligne-numero" style={{ backgroundColor: estSelectionnee ? '#e67e22' : couleur }}>
        {numero}
      </div>
      <div className="ligne-info">
        <span className="ligne-trajet">
          {depart} &rarr; {arrivee}
        </span>
        <span className="ligne-arrets">{arrets} arrets</span>
      </div>
    </div>
  );
}

export default LigneBus;
