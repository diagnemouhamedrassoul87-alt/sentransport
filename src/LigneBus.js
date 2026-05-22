import './LigneBus.css';

function LigneBus({ numero, depart, arrivee, arrets, couleur }) {
  return (
    <div className="ligne-bus">
      <div className="ligne-numero" style={{ backgroundColor: couleur }}>
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