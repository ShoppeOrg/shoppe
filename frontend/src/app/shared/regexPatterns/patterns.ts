class Patterns {
  public regexEmail;
  public regexCode;

  constructor() {

    // This pattern validate email
    this.regexEmail = /[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$/

    // This pattern validates  number in this format ******
    this.regexCode = /^[0-9]{6}$/

  }
}

export const patterns = new Patterns()
