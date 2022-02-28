class Logger {
    private lol: string;
    private static instance: Logger;

    constructor(lol: string) {
        this.lol = lol;
    }

    public static create(lol: string) {
        console.log(this);
        if (!this.instance) {
            this.instance = new Logger(lol);
        }
        console.log(this);

        return this.instance;
    }

    public getLol() {
        return this.lol;
    }
}

const loler = Logger.create('MASHA');
console.log(loler.getLol())