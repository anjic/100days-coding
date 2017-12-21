import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ServerSangroupLinkComponent } from './server-sangroup-link.component';

describe('ServerSangroupLinkComponent', () => {
  let component: ServerSangroupLinkComponent;
  let fixture: ComponentFixture<ServerSangroupLinkComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ServerSangroupLinkComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ServerSangroupLinkComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
