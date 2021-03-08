from sqlalchemy.orm import Session

from backend import models, schemas

def create_matchup(db: Session, match: schemas.MatchCreate):
    """Create a match to the database given a MatchCreate schema."""
    db_match = models.Match(player1_id=match.player1, game_id=match.game)

    db.add(db_match)
    db.commit()
    db.refresh(db_match)

    return db_match
